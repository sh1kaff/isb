from argparse import ArgumentParser
from .utils import read_file, json_to_dict, read_settings

def parse_input_param(input_str: str) -> str:
    if input_str.endswith(".txt"):
        input = read_file(input_str)
        if not input:
            raise ValueError(f"File {input} cannot be blank")

        return input

    return input_str

def parse_key_param(key_str: str) -> str:
    if key_str.endswith(".json"):
        key = json_to_dict(key_str).get("key")
        if not key:
            raise ValueError(f"{key_str} cannot be blank")

        return key

    return key_str

def parse_alpha_param(alpha: str) -> str:
    alpha = alpha.lower()
    if alpha in ("ru", "en"):
        return read_settings()["alphabets"][alpha]

    return alpha 


def add_common_arguments(parser):
    parser.add_argument("-a", "--auto", action="store_true", help="Use variables from config settings.json file")
    parser.add_argument("-i", "--input", type=str, help="Input file with plain text")
    parser.add_argument("-o", "--output", type=str, help="Output file with cipher text")
    parser.add_argument("-u", "--to-upper", action="store_true")

def validate_arguments(args):
    if args.auto and (args.input or args.output or getattr(args, "key", None)):
        raise ValueError("You cannot use --auto together with --input, --output or --key")
    
    if args.subparser_name == "vig":
        if not (args.auto or getattr(args, "key", None)):
            raise ValueError("There must be param --auto or --text or --input")

    if not (args.auto or args.input):
        raise ValueError("There must be param --auto or --input")

def parse_arguments():
    parser = ArgumentParser(
        prog="main.py",
        description=""
    )

    subparsers = parser.add_subparsers(help="Available ciphers", dest="subparser_name")
    
    parser_sub = subparsers.add_parser("sub", help="Substitution cipher")
    parser_sub.add_argument("alpha1", type=str, help="RU, EN or string with alphabet")
    parser_sub.add_argument("alpha2", type=str, help="RU, EN or string with alphabet")
    add_common_arguments(parser_sub)

    parser_caesar = subparsers.add_parser("caesar", help="Caesar cipher")
    parser_caesar.add_argument("alpha", type=str, nargs="?", help="RU, EN or string with alphabet")
    parser_caesar.add_argument("-s" ,"--shift", type=int, default=3)
    add_common_arguments(parser_caesar)

    parser_vig = subparsers.add_parser("vig", help="Vigenere cipher")
    parser_vig.add_argument("alpha", type=str, help="RU, EN or string with alphabet")
    parser_vig.add_argument("-k", "--key", type=str, help="Key string or path to key.json")
    add_common_arguments(parser_vig)
    
    args = parser.parse_args()

    validate_arguments(args)

    return args