def findAndReplace(src: str, target: str, replacement: str) -> str:
    parsedChars = []
    match_count = 0
    for c in src:
        if target[match_count] == c:
            match_count += 1
            if match_count == len(target):
                parsedChars.append(replacement)
                match_count = 0
        else:
            if match_count:
                parsedChars.append(target[:match_count])
                match_count = 0
            parsedChars.append(c)

    return "".join(parsedChars)


if __name__ == "__main__":
    print(findAndReplace("forget about the fox", "fox", "dog"))
