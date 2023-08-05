from . import list, input, confirm, checkbox
from typing import Dict, Callable
from argparse import ArgumentParser

parser = ArgumentParser(prog="sorampt", description="A simple prompt toolkit.")
parser.add_argument(
    "--no-ansi", action="store_true", required=False, help="disable ANSI colors"
)
parser.add_argument(
    "-d", "--default", required=False, help="default answer when cancelled"
)

subparsers = parser.add_subparsers(title="prompt type", required=True)


def main():
    result = parser.parse_args()
    result = vars(result)
    prompt: Callable[..., None] = result.pop("func")
    prompt(**result)
