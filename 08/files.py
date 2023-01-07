def writeToFile(filename: str, text: str) -> None:
    with open(filename, "w") as file_out:
        file_out.write(text)


def appendToFile(filename: str, text: str) -> None:
    with open(filename, "a") as file_out:
        file_out.write(text)


def readFromFile(filename: str) -> str:
    with open(filename) as file_in:
        data = file_in.read()
    return data
