from re import L


def printAsciiTable() -> None:
    """prints the ascii table from 32 (' ') to 126 ('~')"""
    for n in range(32, 127):
        print(f"{n} {chr(n)}")
