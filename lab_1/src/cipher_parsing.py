from argparse import ArgumentParser
from .utils import read_file, json_to_dict, read_settings
from config.messages import *


def parse_input_param(input_str: str) -> str:
    if input_str.endswith(".txt"):
        input_text = read_file(input_str)
        return input_text

    return input_str


def parse_key_param(key_str: str) -> str:
    if key_str.endswith(".json"):
        key = json_to_dict(key_str).get("key", "")
        return key

    return key_str


def parse_alpha_param(alpha_str: str) -> str:
    alpha = alpha_str.lower()
    if alpha in ("ru", "en"):
        alphabets = read_settings().get("alphabets", {})
        return alphabets.get(alpha, "")

    return alpha_str


def add_common_arguments(parser):
    parser.add_argument(
        "-a", "--auto", action="store_true", help=ARG_HELP["auto"]
    )
    parser.add_argument("-i", "--input", type=str, help=ARG_HELP["input"])
    parser.add_argument("-o", "--output", type=str, help=ARG_HELP["output"])
    parser.add_argument(
        "-u", "--to-upper", action="store_true", help=ARG_HELP["uppercase"]
    )


def validate_arguments(args):
    if args.auto and (args.input or args.output or getattr(args, "key", None)):
        raise ValueError(ERRORS["auto_input_conflict_with_key"])

    if args.cipher == "vig":
        if not (args.auto or getattr(args, "key", None)):
            raise ValueError(ERRORS["auto_key_missing"])

    if not (args.auto or args.input):
        raise ValueError(ERRORS["auto_input_missing"])


def parse_arguments():
    parser = ArgumentParser(
        prog="cipher.py",
        description=PROG_DESC["cipher"],
    )

    subparsers = parser.add_subparsers(
        required=True, dest="cipher", description=SUB_PROG_DESC["cipher"], help=SUB_PROG_HELP["cipher"]
    )

    parser_sub = subparsers.add_parser(
        "sub",
        description=SUB_PROG_DESC["sub"],
        help=SUB_PROG_HELP["sub"],
    )
    parser_sub.add_argument("alpha1", type=str, help=ARG_HELP["alpha"])
    parser_sub.add_argument("alpha2", type=str, help=ARG_HELP["alpha"])
    add_common_arguments(parser_sub)

    parser_caesar = subparsers.add_parser(
        "caesar", description=SUB_PROG_DESC["caesar"], help=SUB_PROG_HELP["caesar"]
    )
    parser_caesar.add_argument("alpha", type=str, help=ARG_HELP["alpha"])
    parser_caesar.add_argument(
        "-s", "--shift", type=int, default=3, help=ARG_HELP["shift"]
    )
    add_common_arguments(parser_caesar)

    parser_vig = subparsers.add_parser(
        "vig", description=SUB_PROG_DESC["vig"], help=SUB_PROG_HELP["vig"]
    )
    parser_vig.add_argument("alpha", type=str, help=ARG_HELP["alpha"])
    parser_vig.add_argument("-k", "--key", type=str, help=ARG_HELP["key"])
    add_common_arguments(parser_vig)

    args = parser.parse_args()

    validate_arguments(args)

    return args
