def ordinalSuffix(num: int) -> str:
    suffix = "th"
    if num in range(10, 20):
        suffix = "th"
    elif num % 10 == 1:
        suffix = "st"
    elif num % 10 == 2:
        suffix = "nd"
    elif num % 10 == 3:
        suffix = "rd"
    return f"{num}{suffix}"
