from config.messages import *

def substitution(alphabet1: str, alphabet2: str, message: str, to_upper: bool = False) -> str:
    if not (alphabet1 and alphabet2):
        raise ValueError(ERRORS["alphabets_empty"])

    if not message:
        return ""

    if to_upper:
        alphabet1, alphabet2, message = map(str.upper, (alphabet1, alphabet2. message))

    if len(alphabet1) != len(set(alphabet1)):
        raise ValueError(ERRORS["alphabet1_same_chars"])

    if len(alphabet2) < len(alphabet1):
        raise ValueError(
            ERRORS["alphabet2_shorter"]
        )

    cipher_text = ""

    char_to_char = {char1: char2 for char1, char2 in zip(alphabet1, alphabet2)}

    for char in message:
        if char not in char_to_char:
            cipher_text += char
            continue

        cipher_text += char_to_char[char]

    return cipher_text


def caesar(alphabet: str, message: str, shift: int = 3, to_upper: bool = False) -> str:
    if not alphabet:
        raise ValueError(ERRORS["alphabet_empty"])

    if to_upper:
        alphabet, message = map(str.upper, (alphabet, message))

    if len(alphabet) != len(set(alphabet)):
        raise ValueError(ERRORS["alphabet_contains_same_chars"])


    if not message:
        return ""

    cipher_text = ""

    char_to_index = {char: idx for idx, char in enumerate(alphabet)}

    for char in message:
        if char not in char_to_index:
            cipher_text += char
            continue

        new_idx = (char_to_index[char] + shift) % len(alphabet)
        cipher_text += alphabet[new_idx]

    return cipher_text


def vigenere(alphabet: str, key: str, message: str, to_upper: bool = False) -> str:
    if not key:
        raise ValueError(ERRORS["key_empty"])

    if not alphabet:
        raise ValueError(ERRORS["alphabet_empty"])

    if to_upper:
        alphabet, key, message = map(str.upper, (alphabet, key, message))

    if len(alphabet) != len(set(alphabet)):
        raise ValueError(ERRORS["alphabet_contains_same_chars"])

    if not message:
        return ""

    cipher_text = ""
    alphabet_len = len(alphabet)

    char_to_index = {char: idx for idx, char in enumerate(alphabet)}

    msg_idx = 0
    for msg_char in message:
        key_char = key[msg_idx % len(key)]

        if msg_char not in char_to_index:
            cipher_text += msg_char
            continue

        msg_idx += 1

        if key_char not in char_to_index:
            raise ValueError(ERRORS["key_invalid_char"].format(key_char=key_char))

        shift1 = char_to_index[key_char]
        shift2 = char_to_index[msg_char]

        cipher_text += alphabet[(shift1 + shift2) % alphabet_len]

    return cipher_text


if __name__ == "__main__":
    print(substitution("abcdef", "123456", "aaff-"))
    print(caesar("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ", "АБВЯ-", 1))
    print(vigenere("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ", "МОНАСТЫРЬ", "РАСКИНУЛОСЬМОРЕШИРОКО-"))
