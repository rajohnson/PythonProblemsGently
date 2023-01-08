def getChessSquareColor(col: int, row: int) -> str:
    """Return color of a chess square starting (0 indexed)
    at the upper right corner."""
    if col not in range(8) or row not in range(8):
        return ""
    if (col + row) % 2 == 0:
        return "white"
    return "black"
