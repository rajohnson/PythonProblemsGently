def area(l: float, w: float) -> float:
    if l < 0 or w < 0:
        raise ValueError("cannot have negative side lengths")
    return l * w


def perimeter(l: float, w: float) -> float:
    if l < 0 or w < 0:
        raise ValueError("cannot have negative side lengths")
    return 2 * l + 2 * w


def volume(l: float, w: float, h: float) -> float:
    if l < 0 or w < 0 or h < 0:
        raise ValueError("cannot have negative side lengths")
    return l * w * h


def surfaceArea(l: float, w: float, h: float) -> float:
    if l < 0 or w < 0 or h < 0:
        raise ValueError("cannot have negative side lengths")
    return 2 * (l * w + l * h + h * w)
