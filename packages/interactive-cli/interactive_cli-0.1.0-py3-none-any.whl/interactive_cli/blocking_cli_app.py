from interactive_cli.cli_app import CLIApp


class BlockingCLIApp(CLIApp):
    def start(self) -> None:
        self.running = True
        self.logger.debug("Starting busy loop")

        self.print_start_page()

        while self.running:
            cmd = input()
            self.handle_input(cmd)
