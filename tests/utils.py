from __future__ import annotations

import inspect


def title_format(text: str) -> str:
    """Format a string with title format (line before text + )."""
    return "\n" + "\033[0;30;43m" + text + "\033[0;0m"


def docstring_format(text: str):
    return "\033[3;32m" + inspect.cleandoc(text) + "\033[0;0m"


def show_me(func):
    """Wrapper to show the name of the function and its docstring before running it."""

    def wrapper(*args, **kwargs):
        format_function(func)
        func(*args, **kwargs)
        print("\n")
        return

    return wrapper


def format_function(function_name):
    print(title_format(f"Running {function_name.__name__}():"))
    if function_name.__doc__ is not None:
        print(docstring_format(function_name.__doc__))
