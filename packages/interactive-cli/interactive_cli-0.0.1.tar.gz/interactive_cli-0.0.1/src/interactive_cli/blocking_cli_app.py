from interactive_cli.cli_app import CLIApp


class BlockingCLIApp(CLIApp):
    def start(self) -> None:
        self.running = True
        self.logger.debug("Starting busy loop")

        self.print_interface()

        while self.running:
            self.handle_input(input(self.get_input_message()))

    def stop(self) -> None:
        self.running = False

    def is_running(self) -> bool:
        return self.running
