def add(s: str) -> int:
    if s == "":
        return 0
    return sum(int(n) for n in s.split(","))
