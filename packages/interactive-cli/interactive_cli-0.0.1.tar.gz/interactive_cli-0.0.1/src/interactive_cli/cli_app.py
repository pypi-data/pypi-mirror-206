from collections import defaultdict
from functools import reduce
from logging import getLogger
from typing import DefaultDict, Generator, List, Literal, Optional, Union, cast

from interactive_cli.cli_command import CLICommand, create_help_command, create_quit_command, create_restart_command
from interactive_cli.cli_print_context import CLIHasPrintSettings
from interactive_cli.static import SLUG
from interactive_cli.utils import index


Mode = Literal["flow", "page"]


INPUT_MESSAGE = "\nEnter command [{cmd_list}]: "
INVALID_COMMAND_MESSAGE = "Command '{cmd}' is unknown."
HELP_OVERVIEW_TEXT = "Use '{help_cmd}' to get a detailed list of commands."


class CLIApp(CLIHasPrintSettings):
    name: str
    mode: Mode
    commands: List[CLICommand]

    def __init__(
        self,
        name: str,
        mode: Mode,
        help_command: Union[bool, CLICommand] = True,
        quit_command: Union[bool, CLICommand] = True,
        restart_command: Union[bool, CLICommand] = False
    ) -> None:
        self.logger = getLogger(f"{SLUG}.{self.__class__.__name__}")
        self.name = name
        self.mode = mode
        self.commands = []

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

    def start(self) -> None:
        raise NotImplementedError()

    def stop(self) -> None:
        raise NotImplementedError()

    def is_running(self) -> bool:
        raise NotImplementedError()

    def print_interface(self) -> None:
        self.logger.debug("Rerendering interface")
        help_cmd = self.get_help_command()

        if help_cmd:
            self.print_page(HELP_OVERVIEW_TEXT.format(help_cmd=help_cmd.name), show_title=True)
        else:
            self.print_page(show_title=True)

    def restart(self) -> None:
        self.stop()
        self.start()

    def clear(self) -> None:
        # taken from https://stackoverflow.com/a/50560686/5934316
        self.print("\033[H\033[2J")

    def print_page(self, *values, show_title: Optional[bool] = None) -> None:
        if self.mode == "page":
            self.clear()

        if (show_title is None and self.mode == "page") or show_title:
            self.print_title()

        self.print(*values)
        self.print("")

    def get_help_command(self) -> Optional[CLICommand]:
        for command in self.commands:
            if command.is_help_command:
                return command
        return None

    def print_title(self) -> None:
        self.print(self.name)
        self.print("=" * len(self.name))
        self.print("")

    @property
    def command_short_codes(self) -> Generator[str, None, None]:
        return (command.short_code for command in self.commands)

    @property
    def command_names(self) -> Generator[str, None, None]:
        return (command.name for command in self.commands)

    def get_input_message(self) -> str:
        return INPUT_MESSAGE.format(
            cmd_list=",".join(
                (
                    cmd.short_code
                    for cmd in filter(lambda c: c.show_in_input, self.commands)
                )
            )
        )

    def handle_command(self, command_index: int) -> None:
        self.commands[command_index].execute(self)

    def handle_invalid_command(self, cmd: str) -> None:
        self.print(INVALID_COMMAND_MESSAGE.format(cmd=cmd))

    def handle_input(self, input: str) -> None:
        cmd = input.strip().lower()
        self.logger.debug(f"Received input {cmd}")

        try:
            name_index = index(cmd, self.command_short_codes)
            self.handle_command(name_index)
            return
        except ValueError:
            pass

        try:
            name_index = index(cmd, self.command_names)
            self.handle_command(name_index)
            return
        except ValueError:
            pass

        self.logger.debug(f"Unknown command {cmd}")
        self.handle_invalid_command(cmd)

    def add_help_command(self) -> None:
        self.add_command(create_help_command(), is_help_command=True)

    def add_quit_command(self) -> None:
        self.add_command(create_quit_command())

    def add_restart_command(self) -> None:
        self.add_command(create_restart_command())

    def add_command(self, command: CLICommand, is_help_command: bool = False) -> None:
        if is_help_command:
            for command in self.commands:
                command.is_help_command = False
            command.is_help_command = True

        self.commands.append(command)
        self._validate_command_list()

    def _create_command_short_code_conflicts(self) -> List[List[CLICommand]]:
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
                cast(List[CLICommand], []),
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
                f"The following commands short codes are not unique: {conflict_str}"
            )
