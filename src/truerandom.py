"""
truerandom

Randomization Library for python including complex functions.

```
import truerandom as tr
tr.randomrange(1, 100)
```

"""

import time
import trhelpers as _tr

def random():
    """
    Returns a random float number between 0.0 and 1.0.
    """

    allowed_chars = "0123456789"

    seed = int(time.time() * 1000) % 1000000
    seedL1 = _tr.string_to_base64(str(seed))
    seedL2 = _tr.string_to_base10(seedL1)

    for _ in range(10):
        seedL2 = (seedL2 * 9301 + 49297) % 233280

    return seedL2 / 233280.0
    
def depthrandom(decimals: int = 6):
    """
    Returns a random float number between 0.0 and 1.0 with specified decimal places.
    """

    rand_float = random()
    return round(rand_float, decimals)

def randomrange(start: int, end: int):
    """
    Returns a random integer between start and end (inclusive).
    """

    rand_float = random()
    return int(rand_float * (end - start + 1)) + start

def randomchoice(sequence):
    """
    Returns a random element from a non-empty sequence.
    """

    if not sequence:
        raise ValueError("Cannot choose from an empty sequence")

    rand_index = randomrange(0, len(sequence) - 1)
    return sequence[rand_index]

def randomsample(sequence, k: int):
    """
    Returns a list of k unique random elements from a non-empty sequence.
    """

    if not sequence:
        raise ValueError("Cannot sample from an empty sequence")
    if k > len(sequence):
        raise ValueError("Sample size k cannot be greater than the length of the sequence")

    sampled_indices = set()
    while len(sampled_indices) < k:
        rand_index = randomrange(0, len(sequence) - 1)
        sampled_indices.add(rand_index)

    return [sequence[i] for i in sampled_indices]

def shuffle(sequence):
    """
    Shuffles the elements of a sequence in place.
    """

    if not sequence:
        raise ValueError("Cannot shuffle an empty sequence")

    for i in range(len(sequence) - 1, 0, -1):
        j = randomrange(0, i)
        sequence[i], sequence[j] = sequence[j], sequence[i]

def randomstring(length: int):
    """
    Returns a random string of specified length consisting of uppercase letters, lowercase letters, and digits.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randomhex(length: int):
    """
    Returns a random hexadecimal string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "0123456789abcdef"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randomuuid():
    """
    Returns a random UUID string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-{random_hex_segment(4)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomcolor():
    """
    Returns a random color in hexadecimal format (e.g., #RRGGBB).
    """

    return f"#{randomhex(6)}"

def randombool():
    """
    Returns a random boolean value (True or False).
    """

    return randomchoice([True, False])

def randomdate(start_year: int, end_year: int):
    """
    Returns a random date between January 1st of start_year and December 31st of end_year.
    """

    if start_year > end_year:
        raise ValueError("start_year must be less than or equal to end_year")

    year = randomrange(start_year, end_year)
    month = randomrange(1, 12)

    if month == 2:
        day = randomrange(1, 29)  # Simplified: not accounting for leap years
    elif month in [4, 6, 9, 11]:
        day = randomrange(1, 30)
    else:
        day = randomrange(1, 31)

    return f"{year:04d}-{month:02d}-{day:02d}"

def randomtime():
    """
    Returns a random time in HH:MM:SS format.
    """

    hour = randomrange(0, 23)
    minute = randomrange(0, 59)
    second = randomrange(0, 59)

    return f"{hour:02d}:{minute:02d}:{second:02d}"

def randomdatetime(start_year: int, end_year: int):
    """
    Returns a random datetime string in the format YYYY-MM-DD HH:MM:SS.
    """

    date_part = randomdate(start_year, end_year)
    time_part = randomtime()

    return f"{date_part} {time_part}"

def randomip():
    """
    Returns a random IPv4 address in the format X.X.X.X where X is between 0 and 255.
    """

    return ".".join(str(randomrange(0, 255)) for _ in range(4))

def randommac():
    """
    Returns a random MAC address in the format XX:XX:XX:XX:XX:XX where X is a hexadecimal digit.
    """

    return ":".join(randomhex(2) for _ in range(6))

def randomport():
    """
    Returns a random port number between 0 and 65535.
    """

    return randomrange(0, 65535)

def randomchar():
    """
    Returns a random ASCII character.
    """

    return chr(randomrange(32, 126))  # Printable ASCII range

def randompassword(length: int):
    """
    Returns a random password of specified length consisting of uppercase letters, lowercase letters, digits, and special characters.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/"
    )
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randomuuid4():
    """
    Returns a random UUID4 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-4{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid1():
    """
    Returns a random UUID1 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-1{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid3(namespace: str, name: str):
    """
    Returns a random UUID3 string based on the given namespace and name in the format 8-4-4-4-12.
    """

    import hashlib

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    # Create a hash of the namespace and name
    hash_input = (namespace + name).encode('utf-8')
    hash_output = hashlib.md5(hash_input).hexdigest()

    return f"{hash_output[:8]}-{hash_output[8:12]}-3{hash_output[13:16]}-{hash_output[16:20]}-{hash_output[20:32]}"

def randomuuid5(namespace: str, name: str):
    """
    Returns a random UUID5 string based on the given namespace and name in the format 8-4-4-4-12.
    """

    import hashlib

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    # Create a hash of the namespace and name
    hash_input = (namespace + name).encode('utf-8')
    hash_output = hashlib.sha1(hash_input).hexdigest()

    return f"{hash_output[:8]}-{hash_output[8:12]}-5{hash_output[13:16]}-{hash_output[16:20]}-{hash_output[20:32]}" 

def randomuuid6():
    """
    Returns a random UUID6 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-6{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid7():
    """
    Returns a random UUID7 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-7{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid8():
    """
    Returns a random UUID8 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-8{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid9():
    """
    Returns a random UUID9 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-9{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid10():
    """
    Returns a random UUID10 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-a{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid11():
    """
    Returns a random UUID11 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-b{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid12():
    """
    Returns a random UUID12 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-c{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid13():
    """
    Returns a random UUID13 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-d{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid14():
    """
    Returns a random UUID14 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-e{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid15():
    """
    Returns a random UUID15 string in the format 8-4-4-4-12.
    """

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-f{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randombase2(length: int):
    """
    Returns a random binary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "01"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase3(length: int):
    """
    Returns a random ternary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "012"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase4(length: int):
    """
    Returns a random quaternary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "0123"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase5(length: int):
    """
    Returns a random quinary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "01234"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase6(length: int):
    """
    Returns a random senary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "012345"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase7(length: int):
    """
    Returns a random septenary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "0123456"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase8(length: int):
    """
    Returns a random octal string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "01234567"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase9(length: int):
    """
    Returns a random nonary string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "012345678"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase10(length: int):
    """
    Returns a random decimal string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "0123456789"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase16(length: int):
    """
    Returns a random hexadecimal string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "0123456789abcdef"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase32(length: int):
    """
    Returns a random base32 string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase64(length: int):
    """
    Returns a random base64 string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase85(length: int):
    """
    Returns a random base85 string of specified length.
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")

    allowed_chars = (
        "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
    )
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randombase(base: int, length: int):
    """
    Returns a random string of specified length in the given base (2 to 85).
    """

    if length <= 0:
        raise ValueError("Length must be a positive integer")
    if base < 2 or base > 85:
        raise ValueError("Base must be between 2 and 85")

    allowed_chars = (
        "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
    )[:base]
    return ''.join(randomchoice(allowed_chars) for _ in range(length))

def randomuuid_custom(version: int):
    """
    Returns a random UUID string of specified version (1 to 15) in the format 8-4-4-4-12.
    """

    if version < 1 or version > 15:
        raise ValueError("Version must be between 1 and 15")

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-{version}{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid_by_version(version: int):
    """
    Returns a random UUID string of specified version (1 to 15) in the format 8-4-4-4-12.
    """

    if version < 1 or version > 15:
        raise ValueError("Version must be between 1 and 15")

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    return f"{random_hex_segment(8)}-{random_hex_segment(4)}-{version}{random_hex_segment(3)}-{random_hex_segment(4)}-{random_hex_segment(12)}"

def randomuuid_by_version_and_namespace(version: int, namespace: str, name: str):
    """
    Returns a random UUID string of specified version (1 to 15) based on the given namespace and name in the format 8-4-4-4-12.
    """

    if version < 1 or version > 15:
        raise ValueError("Version must be between 1 and 15")

    import hashlib

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    # Create a hash of the namespace and name
    hash_input = (namespace + name).encode('utf-8')
    if version == 3:
        hash_output = hashlib.md5(hash_input).hexdigest()
    elif version == 5:
        hash_output = hashlib.sha1(hash_input).hexdigest()
    else:
        raise ValueError("Only versions 3 and 5 support namespace-based UUIDs")

    return f"{hash_output[:8]}-{hash_output[8:12]}-{version}{hash_output[13:16]}-{hash_output[16:20]}-{hash_output[20:32]}"

def randomuuid_by_namespace(namespace: str, name: str):
    """
    Returns a random UUID string based on the given namespace and name in the format 8-4-4-4-12.
    """

    import hashlib

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    # Create a hash of the namespace and name
    hash_input = (namespace + name).encode('utf-8')
    hash_output = hashlib.sha1(hash_input).hexdigest()

    return f"{hash_output[:8]}-{hash_output[8:12]}-5{hash_output[13:16]}-{hash_output[16:20]}-{hash_output[20:32]}"

def randomuuid_by_name(name: str):
    """
    Returns a random UUID string based on the given name in the format 8-4-4-4-12.
    """

    import hashlib

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    # Create a hash of the name
    hash_input = name.encode('utf-8')
    hash_output = hashlib.sha1(hash_input).hexdigest()

    return f"{hash_output[:8]}-{hash_output[8:12]}-5{hash_output[13:16]}-{hash_output[16:20]}-{hash_output[20:32]}"

def randomuuid_by_namespace_and_name(namespace: str, name: str):
    """
    Returns a random UUID string based on the given namespace and name in the format 8-4-4-4-12.
    """

    import hashlib

    def random_hex_segment(length):
        return ''.join(randomchoice("0123456789abcdef") for _ in range(length))

    # Create a hash of the namespace and name
    hash_input = (namespace + name).encode('utf-8')
    hash_output = hashlib.sha1(hash_input).hexdigest()

    return f"{hash_output[:8]}-{hash_output[8:12]}-5{hash_output[13:16]}-{hash_output[16:20]}-{hash_output[20:32]}"

def randomdice(sides: int = 6):
    """
    Simulates a dice roll and returns a random integer between 1 and the specified number of sides (inclusive).
    """

    if sides <= 0:
        raise ValueError("Number of sides must be a positive integer")

    return randomrange(1, sides)
