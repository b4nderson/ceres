import re


def sorted_alphanumeric(list):
    def convert(text): return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key): return [
        convert(c) for c in re.split('([0-9]+)', key)
    ]

    return sorted(list, key=alphanum_key)
