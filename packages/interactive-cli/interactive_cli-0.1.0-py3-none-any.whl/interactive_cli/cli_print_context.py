from contextlib import AbstractContextManager
from sys import stdout
from types import TracebackType
from typing import List, Optional, TextIO, Type, TypedDict, Union

try:
    from typing import Unpack  # type: ignore
except ImportError:
    from typing_extensions import Unpack


class PrintArgs(TypedDict, total=False):
    sep: str
    end: str
    file: TextIO
    flush: bool


class _FullPrintArgs(TypedDict):
    sep: str
    end: str
    file: TextIO
    flush: bool


class CLIHasPrintSettings:
    print_prefixes: List[str] = []
    print_suffixes: List[str] = []
    sep: str = " "
    end: str = "\n"
    file: TextIO = stdout
    flush: bool = False

    def _merge_print_args(self, **kwargs: Unpack[PrintArgs]) -> _FullPrintArgs:
        print_args: _FullPrintArgs = {
            "sep": self.sep,
            "end": self.end,
            "file": self.file,
            "flush": self.flush,
        }
        print_args.update(kwargs)  # type: ignore
        return print_args

    def print(self, *values, **kwargs: Unpack[PrintArgs]) -> None:
        print_args = self._merge_print_args(**kwargs)

        if self.print_prefixes:
            print(
                *self.print_prefixes,
                sep="",
                end="",
                file=print_args["file"],
                flush=print_args["flush"],
            )

        print(
            *values,
            sep=print_args["sep"],
            end="",
            file=print_args["file"],
            flush=print_args["flush"],
        )

        print(
            *self.print_suffixes,
            sep="",
            end=print_args["end"],
            file=print_args["file"],
            flush=print_args["flush"],
        )

    def indent_context(self, indent: Union[str, int] = 2) -> "IndentCLIPrintContext":
        return IndentCLIPrintContext(self, indent)


class CLIPrintContext(AbstractContextManager):
    printer: CLIHasPrintSettings

    def __init__(self, printer: CLIHasPrintSettings) -> None:
        self.printer = printer

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        return None


class BufferedPrintOut(CLIPrintContext):
    buffer: TextIO
    original_file: TextIO

    def __init__(self, printer: CLIHasPrintSettings, buffer: TextIO) -> None:
        super().__init__(printer)
        self.buffer = buffer

    def __enter__(self) -> None:
        self.original_file = self.printer.file
        self.printer.file = self.buffer

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        super().__exit__(exc_type, exc_value, traceback)
        self.printer.file = self.original_file
        return None


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

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        super().__exit__(exc_type, exc_value, traceback)
        self.printer.print_prefixes.pop()
        return None
