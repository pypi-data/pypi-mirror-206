from tabulate import tabulate
from typing import TYPE_CHECKING, Any, Callable, Optional

if TYPE_CHECKING:
    from interactive_cli.cli_app import CLIApp


class CLICommand:
    name: str
    action: Callable[["CLIApp"], None]
    _short_code: Optional[str]
    description: Optional[str]

    is_help_command: bool = False
    show_in_input: bool = True

    def __init__(
        self,
        name: str,
        action: Callable[["CLIApp"], None],
        description: Optional[str] = None,
        short_code: Optional[str] = None,
    ) -> None:
        if len(name) == 0:
            raise ValueError("Empty string is not allowed as a command")

        self.name = name
        self.action = action
        self.description = description
        self._short_code = short_code

    def execute(self, app: "CLIApp") -> None:
        self.action(app)

    @property
    def short_code(self) -> str:
        if self._short_code is None:
            return self.name[0]
        return self._short_code

    @short_code.setter
    def short_code(self, value: Optional[str]) -> None:
        self._short_code = value

    def __call__(self, app: "CLIApp") -> Any:
        self.execute(app)


def _render_help(app: "CLIApp") -> None:
    app.print_page(
        tabulate(
            (
                (f"{command.name}, {command.short_code}", command.description)
                for command in app.commands
            ),
            tablefmt="plain"
        )
    )


def create_help_command() -> CLICommand:
    return CLICommand("help", _render_help, "Show all commands")

def create_quit_command() -> CLICommand:
    return CLICommand("quit", lambda app: app.stop(), "Quit the program")

def create_restart_command() -> CLICommand:
    return CLICommand("restart", lambda app: app.restart(), "Restart the program")
