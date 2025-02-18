def substitution(alphabet1: str, alphabet2: str, message: str) -> str:
    cipher_text = ""

    for char in message:
        idx = alphabet1.find(char)
        if idx == -1:
            cipher_text += char
            continue
        
        cipher_text += alphabet2[idx]
    
    return message

def caesar(alphabet: str, shift: int, message: str) -> str:
    pass