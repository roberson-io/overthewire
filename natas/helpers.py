def between(s: str, start: str, end: str) -> str:
    return s[s.find(start) + len(start) : s.rfind(end)]
