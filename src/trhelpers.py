def string_to_base64(text: str) -> str:
    base64_chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    )

    data_bytes = text.encode("utf-8")
    binary_str = "".join(f"{byte:08b}" for byte in data_bytes)

    remainder = len(binary_str) % 6
    if remainder != 0:
        binary_str += "0" * (6 - remainder)

    encoded = []
    for i in range(0, len(binary_str), 6):
        chunk = binary_str[i : i + 6]
        index = int(chunk, 2)
        encoded.append(base64_chars[index])

    result = "".join(encoded)
    padding_needed = (4 - len(result) % 4) % 4
    return result + ("=" * padding_needed)

def string_to_base10(text: str):
    total = 0
    for char in text:
        digit = ord(char) - ord("0")
        total = (total * 10) + digit
    return total

