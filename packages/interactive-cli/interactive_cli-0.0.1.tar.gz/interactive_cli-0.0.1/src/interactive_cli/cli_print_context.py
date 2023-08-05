from dataclasses import dataclass
from sys import stdout
from typing import List, TextIO, Union


class CLIHasPrintSettings:
    print_prefixes: List[str] = []
    print_suffixes: List[str] = []
    print_sep: str = " "
    print_end: str = "\n"
    print_file: TextIO = stdout
    print_flush: bool = False

    def print(self, *values) -> None:
        if self.print_prefixes:
            print(
                *self.print_prefixes,
                sep="",
                end="",
                file=self.print_file,
                flush=self.print_flush,
            )

        print(
            *values,
            sep=self.print_sep,
            end="",
            file=self.print_file,
            flush=self.print_flush,
        )

        print(
            *self.print_suffixes,
            sep="",
            end=self.print_end,
            file=self.print_file,
            flush=self.print_flush,
        )

    def with_indent(self, indent: Union[str, int] = 2) -> "IndentCLIPrintContext":
        return IndentCLIPrintContext(self, indent)


class CLIPrintContext:
    printer: CLIHasPrintSettings

    def __init__(self, printer: CLIHasPrintSettings) -> None:
        self.printer = printer

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(self, *args):
        raise NotImplementedError()


class IndentCLIPrintContext(CLIPrintContext):
    indent: Union[str, int]

    def __init__(
        self, printer: CLIHasPrintSettings, indent: Union[str, int] = 2
    ) -> None:
        super().__init__(printer)
        self.indent = indent

    def __enter__(self) -> None:
        self.printer.print_prefixes.append(
            self.indent if isinstance(self.indent, str) else " " * self.indent
        )

    def __exit__(self) -> None:
        self.printer.print_prefixes.pop()
