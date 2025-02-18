def substitution(alphabet1: str, alphabet2: str, message: str) -> str:
    if len(alphabet1) != len(set(alphabet1)):
        raise ValueError("Alphabet1 contains the same characters")
    
    if len(alphabet2) != len(set(alphabet2)):
        raise ValueError("Alphabet2 contains the same characters")

    if len(alphabet1) > len(alphabet2):
        raise ValueError("Alphabet2 len less then Alphabet1 len")
    
    cipher_text = ""

    for char in message:
        idx = alphabet1.find(char)
        if idx == -1:
            cipher_text += char
            continue
        
        cipher_text += alphabet2[idx]
    
    return cipher_text

def caesar(alphabet: str, message: str, shift: int = 3) -> str:
    cipher_text = ""

    for char in message:
        idx = alphabet.find(char)
        if idx == -1:
            cipher_text += char
            continue

        new_idx = (idx + shift) % len(alphabet)
        cipher_text += alphabet[new_idx]

    return cipher_text


if __name__ == "__main__":
    text = "abcdef"
    cipher_text = caesar(text, text, 10)

    print(cipher_text)