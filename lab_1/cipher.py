import src.ciphers as ciphers
from src.utils import write_to_file, read_settings
from src.parsing import parse_arguments, parse_input_param, parse_alpha_param, parse_key_param


def cipher():
    args = parse_arguments()

    result = ""

    if args.auto:
        task1_settings = read_settings().get("task1", {})
        plain_text = parse_input_param(task1_settings.get("plain_text", ""))
        output_file = task1_settings.get("cipher_text", "")
    else:
        plain_text = parse_input_param(args.input)
        output_file = args.output

    match args.cipher:
        case "sub":
            alpha1 = parse_alpha_param(args.alpha1)
            alpha2 = parse_alpha_param(args.alpha2)
            result = ciphers.substitution(alpha1, alpha2, plain_text, args.to_upper)
        case "caesar":
            alpha = parse_alpha_param(args.alpha)
            result = ciphers.caesar(alpha, plain_text, args.shift, args.to_upper)
        case "vig":
            alpha = parse_alpha_param(args.alpha)
            if args.auto:
                key = parse_key_param(task1_settings.get("key", ""))
            else:
                key = parse_key_param(args.key)

            result = ciphers.vigenere(alpha, key, plain_text, args.to_upper)

    print(f"Result cipher text:\n{result}")

    if output_file:
        write_to_file(output_file, result)
        print(f"Writing to file {output_file}")


def main():
    try:
        cipher()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
