def findAndReplace(src: str, target: str, replacement: str) -> str:
    parsedChars = []
    n = 0
    while n < len(src):
        if src[n : n + len(target)] == target:
            parsedChars.append(replacement)
            n += len(target)
        else:
            parsedChars.append(src[n])
            n += 1

    return "".join(parsedChars)
