from typing import TYPE_CHECKING, Callable, Optional


if TYPE_CHECKING:
    from interactive_cli.cli_app import CLIApp
    from interactive_cli.cli_page import CLIPage


class CLICommand:
    name: str
    action: Callable[["CLIApp", "CLIPage"], None]
    _short_code: Optional[str]
    description: Optional[str]

    is_help_command: bool = False
    show_in_input: bool = True

    def __init__(
        self,
        name: str,
        action: Callable[["CLIApp", "CLIPage"], None],
        description: Optional[str] = None,
        short_code: Optional[str] = None,
    ) -> None:
        if len(name) == 0:
            raise ValueError("Empty string is not allowed as a command")

        self.name = name
        self.action = action
        self.description = description
        self._short_code = short_code

    def execute(self, app: "CLIApp", page: "CLIPage") -> None:
        self.action(app, page)

    @property
    def short_code(self) -> str:
        if self._short_code is None:
            return self.name[0]
        return self._short_code

    @short_code.setter
    def short_code(self, value: Optional[str]) -> None:
        self._short_code = value
