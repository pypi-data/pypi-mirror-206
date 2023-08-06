from logging import getLogger
from os import name as os_name, system
from sys import stdin
from typing import Callable, List, Literal, TextIO, Union

try:
    from typing import Unpack  # type: ignore
except ImportError:
    from typing_extensions import Unpack

from interactive_cli.cli_command import CLICommand
from interactive_cli.cli_page import CLIPageBase, CLIDefaultPage, CLIPage
from interactive_cli.cli_print_context import PrintArgs
from interactive_cli.static import DEFAULT_PAGE_NAME, SLUG
from interactive_cli.utils import index


class CLIApp(CLIPageBase):
    running: bool
    pages: List[CLIPage]
    current_page_index: int

    stdin: TextIO = stdin
    cursor_pos: Literal["same-line", "separate-ine"] = "same-line"
    use_ansi: bool = True

    def __init__(
        self,
        name: str,
        default_page: Union[Literal[True], Callable[["CLIApp"], CLIPage]] = True,
        help_command: Union[bool, "CLICommand"] = True,
        quit_command: Union[bool, "CLICommand"] = True,
        restart_command: Union[bool, "CLICommand"] = False,
    ) -> None:
        self.running = False
        self.pages = []
        self.current_page_index = 0
        if callable(default_page):
            self.add_page(default_page(self))
        else:
            self.add_page(CLIDefaultPage(self, DEFAULT_PAGE_NAME, False))

        super().__init__(name, help_command, quit_command, restart_command)

        self.logger = getLogger(f"{SLUG}.{self.__class__.__name__}")

    def start(self) -> None:
        raise NotImplementedError()

    def stop(self) -> None:
        self.running = False

    def is_running(self) -> bool:
        return self.running

    def restart(self) -> None:
        self.stop()
        self.start()

    def add_page(self, page: CLIPage) -> None:
        self.pages.append(page)

    def get_index(self, page: Union[int, str, CLIPage]) -> int:
        if isinstance(page, int):
            if page < 0 or page >= len(self.pages):
                raise IndexError(
                    f"Page {page} does not exist. Page must be 0 <= page < "
                    f"{len(self.pages)}"
                )
            return page

        for i, p in enumerate(self.pages):
            if (isinstance(page, str) and page == p.name) or (
                isinstance(page, CLIPage) and page == p
            ):
                return i

        raise KeyError(f"Could not find page {page}")

    def get_page(self, page: Union[int, str, CLIPage]) -> CLIPage:
        return self.pages[self.get_index(page)]

    def show_page(
        self, page: Union[int, str, CLIPage], *fallback: Union[int, str, CLIPage]
    ) -> None:
        for p in [page] + list(fallback):
            try:
                self.current_page_index = self.get_index(p)
                self.current_page.print_interface()
                return
            except (IndexError, KeyError):
                pass

    def print_start_page(self) -> None:
        self.pages[0].print_interface()

    def clear_console(self) -> None:
        if self.use_ansi:
            # taken from https://stackoverflow.com/a/50560686/5934316
            self.print_to_console("\033[H\033[2J")
        elif os_name == "nt":
            system("cls")
        else:
            system("clear")

    def print_header(self) -> None:
        self.print_to_console(self.name)
        self.print_to_console("=" * len(self.name))
        self.print_to_console("")

    def print_footer(self) -> None:
        self.print_to_console("")
        self.print_to_console(self.current_page.get_input_message(), end="")

    def add_command(self, command: "CLICommand", is_help_command: bool = False) -> None:
        self.current_page.add_command(command, is_help_command)

    def print_page(
        self,
        *values,
        clear: bool = True,
        show_title: bool = True,
        **kwargs: Unpack[PrintArgs],
    ) -> None:
        self.current_page.print_page(
            *values, clear=clear, show_title=show_title, **kwargs
        )

    def print_to_console(self, *values, **kwargs: Unpack[PrintArgs]) -> None:
        super().print(*values, **kwargs)

    def print(
        self,
        *values,
        to: Literal["page", "console"] = "page",
        **kwargs: Unpack[PrintArgs],
    ) -> None:
        if to == "page":
            self.print_page(*values, clear=False, **kwargs)
        else:
            self.print_to_console(*values, **kwargs)

    @property
    def stdout(self) -> TextIO:
        return self.file

    @stdout.setter
    def stdout(self, value: TextIO) -> None:
        self.file = value

    @stdout.deleter
    def stdout(self) -> None:
        raise AttributeError("Cannot delete stdout")

    @property
    def current_page(self) -> CLIPage:
        try:
            return self.pages[self.current_page_index]
        except IndexError as e:
            raise RuntimeError("No pages are added yet") from e

    @current_page.setter
    def current_page(self, value: Union[int, str, CLIPage]) -> None:
        self.show_page(value)

    @current_page.deleter
    def current_page(self) -> None:
        raise AttributeError("Cannot delete current_page")

    def handle_input(self, input: str) -> None:
        cmd = input.strip().lower()
        page = self.current_page
        self.logger.debug(f"Received input {cmd}")

        try:
            name_index = index(cmd, page.command_short_codes)
            page.handle_command(name_index)
            return
        except ValueError:
            pass

        try:
            name_index = index(cmd, page.command_names)
            page.handle_command(name_index)
            return
        except ValueError:
            pass

        self.logger.debug(f"Unknown command {cmd}")
        page.handle_invalid_command(cmd)
