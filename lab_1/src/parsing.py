from argparse import ArgumentParser
from .utils import read_file, json_to_dict, read_settings


def parse_input_param(input_str: str) -> str:
    if input_str.endswith(".txt"):
        input = read_file(input_str)
        return input

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
        "-a", "--auto", action="store_true", help="Using values from the settings.json file"
    )
    parser.add_argument("-i", "--input", type=str, help="Input text or path to text.txt")
    parser.add_argument("-o", "--output", type=str, help="Output file for encrypted text")
    parser.add_argument(
        "-u", "--to-upper", action="store_true", help="Bring all input data to UPPER CASE"
    )


def validate_arguments(args):
    if args.auto and (args.input or args.output or getattr(args, "key", None)):
        raise ValueError("You cannot use --auto together with --input, --output or --key")

    if args.cipher == "vig":
        if not (args.auto or getattr(args, "key", None)):
            raise ValueError("The --auto or --key parameters must be specified")

    if not (args.auto or args.input):
        raise ValueError("The --auto or --input parameters must be specified")


def parse_arguments():
    parser = ArgumentParser(
        prog="cipher.py",
        description="The program encrypts the required text using substitution, Caesar and Vigenère ciphers.",
    )

    subparsers = parser.add_subparsers(
        required=True, dest="cipher", help="Available ciphers (substitution, Caesar, Vigenère)"
    )

    parser_sub = subparsers.add_parser(
        "sub",
        help="Substitution cipher",
        description="Encrypts the text using a substitution cipher",
    )
    parser_sub.add_argument("alpha1", type=str, help="RU, EN or alphabetical string")
    parser_sub.add_argument("alpha2", type=str, help="RU, EN or alphabetical string")
    add_common_arguments(parser_sub)

    parser_caesar = subparsers.add_parser(
        "caesar", help="Caesar cipher", description="Encrypts the text using a Caesar cipher"
    )
    parser_caesar.add_argument("alpha", type=str, nargs="?", help="RU, EN or alphabetical string")
    parser_caesar.add_argument(
        "-s", "--shift", type=int, default=3, help="A shift in Caesar's cipher (can be neg or pos)"
    )
    add_common_arguments(parser_caesar)

    parser_vig = subparsers.add_parser(
        "vig", help="Vigenère cipher", description="Encrypts the text using a Vigenère cipher"
    )
    parser_vig.add_argument("alpha", type=str, help="RU, EN or alphabetical string")
    parser_vig.add_argument("-k", "--key", type=str, help="Key string or path to key.json")
    add_common_arguments(parser_vig)

    args = parser.parse_args()

    validate_arguments(args)

    return args
