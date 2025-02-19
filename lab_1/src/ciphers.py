def substitution(alphabet1: str, alphabet2: str, message: str, to_upper: bool = False) -> str:
    if len(alphabet1) != len(set(alphabet1)):
        raise ValueError("Alphabet1 contains the same characters")
    
    if len(alphabet2) != len(set(alphabet2)):
        raise ValueError("Alphabet2 contains the same characters")

    if len(alphabet1) > len(alphabet2):
        raise ValueError("Alphabet2 len less then Alphabet1 len")
    
    cipher_text = ""

    char_to_char = {char1: char2 for char1, char2 in zip(alphabet1, alphabet2)}

    if to_upper:
        alphabet1 = alphabet1.upper()
        alphabet2 = alphabet2.upper()
        message = message.upper()

    for char in message:
        if char not in char_to_char:
            cipher_text += char
            continue
        
        cipher_text += char_to_char[char]
    
    return cipher_text

def caesar(alphabet: str, message: str, shift: int = 3, to_upper: bool = False) -> str:
    cipher_text = ""

    char_to_index = {char: idx for idx, char in enumerate(alphabet)}

    if to_upper:
        alphabet = alphabet.upper()
        message = message.upper()

    for char in message:
        if char not in char_to_index:
            cipher_text += char
            continue

        new_idx = (char_to_index[char] + shift) % len(alphabet)
        cipher_text += alphabet[new_idx]

    return cipher_text


def vigenere(alphabet: str, key: str, message: str, to_upper: bool = False) -> str:
    cipher_text = ""
    alphabet_len = len(alphabet)

    char_to_index = {char: idx for idx, char in enumerate(alphabet)}

    if to_upper:
        alphabet = alphabet.upper()
        key = key.upper()
        message = message.upper()

    msg_idx = 0
    for msg_char in message:
        key_char = key[msg_idx % len(key)]

        if msg_char not in char_to_index:
            cipher_text += msg_char
            continue

        msg_idx += 1

        if key_char not in char_to_index: 
            raise ValueError(f"Key contains invalid character: '{key_char}'")
        
        shift1 = char_to_index[key_char]
        shift2 = char_to_index[msg_char]
        
        cipher_text += alphabet[(shift1 + shift2) % alphabet_len]
    
    return cipher_text



if __name__ == "__main__":
    print(substitution("abcdef", "123456", "aaff-"))
    print(caesar("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ", "АБВЯ-", 1))
    print(vigenere("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ", "МОНАСТЫРЬ", "РАСКИНУЛОСЬМОРЕШИРОКО-"))