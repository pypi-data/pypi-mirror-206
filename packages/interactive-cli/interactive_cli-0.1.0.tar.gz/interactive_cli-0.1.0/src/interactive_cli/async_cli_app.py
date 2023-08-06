from asyncio import get_event_loop
from sys import stdin
from typing import TextIO


from interactive_cli.cli_app import CLIApp


class AsyncCLIApp(CLIApp):
    async def start(self) -> None:
        self.running = True
        self.logger.debug("Starting async loop")

        self.print_start_page()

        while self.running:
            cmd = await async_input(self.stdin)
            self.handle_input(cmd)

    def print_footer(self) -> None:
        super().print_footer()

        if self.cursor_pos == "same-line":
            # async cli needs a new line to terminate the output

            if not self.use_ansi:
                raise RuntimeError(
                    "Cannot use the curser in the same line with disabled ansi for the "
                    "async console. Please enable ansi or use "
                    "cursor_pos='separate-line'."
                )

            self.print_to_console("")  # add a new line to terminate output
            self.print_to_console(
                # move up cursor two lines
                "\033[3A"
                # move cursor backwards
                f"\033[{len(self.current_page.get_input_message())}C"
            )


async def async_input(stream_in: TextIO = stdin) -> str:
    loop = get_event_loop()
    line = await loop.run_in_executor(None, stream_in.readline)
    return line.strip("\n\r")
