from collections import defaultdict
from functools import reduce
from io import StringIO
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    DefaultDict,
    Generator,
    List,
    Optional,
    Union,
    cast,
)
from tabulate import tabulate

try:
    from typing import Unpack  # type: ignore
except ImportError:
    from typing_extensions import Unpack

if TYPE_CHECKING:
    from interactive_cli.cli_app import CLIApp

from interactive_cli.cli_command import CLICommand
from interactive_cli.cli_print_context import (
    BufferedPrintOut,
    CLIHasPrintSettings,
    PrintArgs,
)
from interactive_cli.static import (
    HELP_OVERVIEW_TEXT,
    INPUT_MESSAGE,
    DEFAULT_PAGE_NAME,
    INVALID_COMMAND_MESSAGE,
)


class CLIPageBase(CLIHasPrintSettings):
    def __init__(
        self,
        name: str,
        help_command: Union[bool, "CLICommand"] = True,
        quit_command: Union[bool, "CLICommand"] = True,
        restart_command: Union[bool, "CLICommand"] = False,
    ) -> None:
        self.name = name

        if isinstance(help_command, CLICommand):
            self.add_command(help_command, is_help_command=True)
        elif help_command:
            self.add_help_command()

        if isinstance(quit_command, CLICommand):
            self.add_command(quit_command)
        elif quit_command:
            self.add_quit_command()

        if isinstance(restart_command, CLICommand):
            self.add_command(restart_command)
        elif restart_command:
            self.add_restart_command()

    def add_help_command(self) -> None:
        self.add_command(create_help_command(), is_help_command=True)

    def add_quit_command(self) -> None:
        self.add_command(create_quit_command())

    def add_restart_command(self) -> None:
        self.add_command(create_restart_command())

    def add_command(self, command: "CLICommand", is_help_command: bool = False) -> None:
        raise NotImplementedError()

    def print_page(
        self,
        *values,
        clear: bool = True,
        show_title: bool = True,
        **kwargs: Unpack[PrintArgs],
    ) -> None:
        raise NotImplementedError()


class CLIPage(CLIPageBase):
    app: "CLIApp"
    name: str
    commands: List["CLICommand"]
    interface: Optional[Union[str, Callable[["CLIApp", "CLIPage"], None]]]

    buffer: StringIO

    def __init__(
        self,
        app: "CLIApp",
        name: str,
        back_command: Union[bool, "CLICommand"] = True,
        interface: Optional[Union[Any, Callable[["CLIApp", "CLIPage"], None]]] = None,
    ) -> None:
        self.app = app
        self.name = name
        self.interface = interface
        self.commands = []

        self.clear_output_buffer()

        if isinstance(back_command, CLICommand):
            self.add_command(back_command, is_help_command=True)
        elif back_command:
            self.add_back_command()

    def clear_output_buffer(self) -> None:
        self.buffer = StringIO()

    def print_interface(self) -> None:
        if callable(self.interface):
            self.interface(self.app, self)
        elif self.interface is not None:
            self.print_page(self.interface)
        else:
            self.print_page()

    def print_buffer(self) -> None:
        self.app.print_to_console(self.buffer.getvalue())

    def print_page(
        self,
        *values,
        clear: bool = True,
        show_title: bool = True,
        **kwargs: Unpack[PrintArgs],
    ) -> None:
        self.app.clear_console()

        if clear:
            self.clear_output_buffer()

        if show_title:
            self.app.print_header()

        if len(values) > 0:
            # print to buffer first to keep custom separator and end characters
            with BufferedPrintOut(self, self.buffer):
                super().print(*values, **kwargs)

        self.print_buffer()

        self.app.print_footer()

    def print(self, *values, **kwargs: Unpack[PrintArgs]) -> None:
        self.print_page(*values, clear=False, **kwargs)

    @property
    def command_short_codes(self) -> Generator[str, None, None]:
        return (command.short_code for command in self.commands)

    @property
    def command_names(self) -> Generator[str, None, None]:
        return (command.name for command in self.commands)

    def add_back_command(self) -> None:
        self.add_command(create_back_command())

    def get_input_message(self) -> str:
        return INPUT_MESSAGE.format(
            cmd_list=",".join(
                (
                    cmd.short_code
                    for cmd in filter(lambda c: c.show_in_input, self.commands)
                )
            )
        )

    def get_help_command(self) -> Optional["CLICommand"]:
        for command in self.commands:
            if command.is_help_command:
                return command
        return None

    def handle_invalid_command(self, cmd: str) -> None:
        self.print(INVALID_COMMAND_MESSAGE.format(cmd=cmd))

    def handle_command(self, command_index: int) -> None:
        self.commands[command_index].execute(self.app, self)

    def add_command(self, command: "CLICommand", is_help_command: bool = False) -> None:
        if is_help_command:
            for cmd in self.commands:
                cmd.is_help_command = False
            command.is_help_command = True

        self.commands.append(command)
        self._validate_command_list()

    def _create_command_short_code_conflicts(self) -> List[List["CLICommand"]]:
        short_code_counts: DefaultDict[str, int] = defaultdict(int)
        for command in self.commands:
            short_code_counts[command.short_code] += 1

        duplicate_short_codes = reduce(
            lambda carry, element: carry + [element[0]] if element[1] > 1 else carry,
            short_code_counts.items(),
            cast(List[str], []),
        )

        conflicts = []
        for duplicate_short_code in duplicate_short_codes:
            commands = reduce(
                lambda carry, element: carry + [element]
                if element.short_code == duplicate_short_code
                else carry,
                self.commands,
                cast(List["CLICommand"], []),
            )

            if len(commands) > 0:
                conflicts.append(commands)

        return conflicts

    def _validate_command_list(self) -> None:
        if len(set(self.command_short_codes)) < len(list(self.command_short_codes)):
            conflicts = self._create_command_short_code_conflicts()
            conflict_str = "; ".join(
                (
                    f"{', '.join((c.name for c in cmds))} for {cmds[0].short_code}"
                    for cmds in conflicts
                )
            )

            raise ValueError(
                f"On page '{self.name}' the following commands short codes are not "
                f"unique: {conflict_str}"
            )


class CLIDefaultPage(CLIPage):
    def print_interface(self) -> None:
        help_cmd = self.get_help_command()

        if help_cmd:
            self.print_page(HELP_OVERVIEW_TEXT.format(help_cmd=help_cmd.name))
        else:
            self.print_page()


def _render_help(app: "CLIApp", page: "CLIPage") -> None:
    app.print_page(
        tabulate(
            (
                (f"{command.name}, {command.short_code}", command.description)
                for command in page.commands
            ),
            tablefmt="plain",
        )
    )


def create_help_command() -> "CLICommand":
    return CLICommand("help", _render_help, "Show all commands")


def create_quit_command() -> "CLICommand":
    return CLICommand("quit", lambda app, _: app.stop(), "Quit the program")


def create_restart_command() -> "CLICommand":
    return CLICommand("restart", lambda app, _: app.restart(), "Restart the program")


def create_back_command() -> "CLICommand":
    return CLICommand(
        "back",
        lambda app, _: app.show_page(DEFAULT_PAGE_NAME, 0),
        "Go back to the previous page",
    )
