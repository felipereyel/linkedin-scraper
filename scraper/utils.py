import re


def extract_number(text: str) -> int:
    return int(re.sub(r"[^\d]", "", text))
