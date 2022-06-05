def add(s: str) -> int:
    if s == "":
        return 0

    s = s.replace("\n", ",")

    return sum(int(n) for n in s.split(","))
