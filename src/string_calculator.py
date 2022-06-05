def get_delimiter(s: str) -> str:
    if s[:2] == "//":
        return s[2], s[3:]

    return ",", s


def add(s: str) -> int:
    if s == "":
        return 0

    delimiter, s = get_delimiter(s)
    s = s.replace("\n", delimiter)

    numbers = [int(n) for n in s.split(delimiter) if n != ""]
    if min(numbers) < 0:
        msg = f"negatives not allowed: {[n for n in numbers if n < 0]}"
        raise Exception(msg)

    return sum(numbers)
