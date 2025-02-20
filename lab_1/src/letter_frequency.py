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