from argparse import ArgumentParser
from src.letter_frequency import calculate_frequency, replace_by_freq
from src.utils import read_settings, get_frequency, write_to_file
from src.cipher_parsing import add_common_arguments, parse_input_param
from config.messages import *

def parse_arguments():
    parser = ArgumentParser(
        prog="analysis.py",
        description=PROG_DESC["analysis"],
    )

    parser.add_argument("-aq", "--alpha-freq", type=str, choices=("ru", "en"), default="ru", help=ARG_HELP["alpha_freq"])
    add_common_arguments(parser)

    args = parser.parse_args()

    if args.auto and (args.input or args.output):
        raise ValueError(ERRORS["auto_input_conflict_without_key"])

    if not (args.auto or args.input):
        raise ValueError(ERRORS["auto_input_missing"])

    return args

def analysis():
    args = parse_arguments()

    if args.auto:
        task2_settings = read_settings().get("task2", {})
        cipher_text = parse_input_param(task2_settings.get("cipher_text", ""))
        output_file = task2_settings.get("plain_text", "")
    else:
        cipher_text = parse_input_param(args.input)
        output_file = args.output


    real_freq = get_frequency(args.alpha_freq)

    cip_freq = calculate_frequency(cipher_text)

    plain_text = replace_by_freq(cipher_text, cip_freq, real_freq)

    print(f"Result plain text:\n{plain_text}")

    if output_file:
        write_to_file(output_file, plain_text)
        print(f"Writing to file {output_file}")


def main():
    try:
        analysis()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()