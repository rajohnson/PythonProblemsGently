def area(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("cannot have negative side lengths")
    return length * width


def perimeter(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("cannot have negative side lengths")
    return 2 * length + 2 * width


def volume(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("cannot have negative side lengths")
    return length * width * height


def surfaceArea(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("cannot have negative side lengths")
    return 2 * (length * width + length * height + height * width)
