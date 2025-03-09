def calculate_frequency(message: str, skip_break: bool = True) -> list:
    result = []
    if not message:
        return result
    
    message_len = len(message)

    for char in set(message):
        if skip_break and char == "\n":
            continue

        frequency = round(message.count(char) / message_len, 6)
        result.append((char, frequency))
    
    result.sort(key=lambda _: _[1], reverse=True)

    return result


def replace_by_freq(text: str, cip_freq: dict, real_freq: dict) -> str:
    replace_dict = {}

    for cip, real in zip(cip_freq, real_freq):
        replace_dict[cip[0]] = real[0]
        print(f"'{cip[0]}' => '{real[0]}'")

    replaced_text = "".join(replace_dict.get(char, char) for char in text)

    return replaced_text


# delete this??
def texts_to_key(alpha: str, plain_text: str, cipher_text: str, to_upper: bool = True) -> str:
    char2char = {}

    if to_upper:
        plain_text, cipher_text, alpha = map(str.upper, (plain_text, cipher_text, alpha))

    for c1, c2 in zip(plain_text, cipher_text):
        char2char.setdefault(c1, c2)


    key = "".join(char2char.get(c, c) for c in alpha)

    return key
