import src.ciphers as ciphers
from src.parsing import parse_arguments, parse_input_param, parse_alpha_param, parse_key_param

def main():
    args = parse_arguments()

    ciphere_text = ""

    plain_text = parse_input_param(args.input)

    match args.subparser_name:
        case "sub":
            alpha1 = parse_alpha_param(args.alpha1)
            alpha2 = parse_alpha_param(args.alpha2)
            ciphere_text = ciphers.substitution(alpha1, alpha2, plain_text, args.to_upper)
        case "caesar": 
            alpha = parse_alpha_param(args.alpha)
            ciphere_text = ciphers.caesar(alpha, plain_text, args.shift, args.to_upper)
        case "vig": 
            alpha = parse_alpha_param(args.alpha)
            key = parse_key_param(args.key)
            ciphere_text = ciphers.vigenere(alpha, key, plain_text, args.to_upper)

    print(ciphere_text)


if __name__ == "__main__":
    main()