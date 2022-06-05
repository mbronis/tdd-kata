import re
from typing import List, Tuple


def get_delimiter(s: str) -> Tuple[List, str]:
    regex = r"^\/{2}\[(.*?)\]"
    delimiter_regex = re.compile(regex)
    delimiter_match = delimiter_regex.match(s)
    if delimiter_match:
        delimiters = delimiter_match.groups()
        return list(delimiters), re.sub(regex, "", s)

    if s[:2] == "//":
        return [s[2]], s[3:]

    return [], s


def add(s: str) -> int:
    if s == "":
        return 0

    delimiters, s = get_delimiter(s)
    delimiters.append("\n")
    for d in delimiters:
        s = s.replace(d, ",")
    # print(delimiter)
    # print(s)

    numbers = [int(n) for n in s.split(",") if (n != "") and (int(n) < 1000)]
    if min(numbers) < 0:
        msg = f"negatives not allowed: {[n for n in numbers if n < 0]}"
        raise Exception(msg)

    return sum(numbers)
