def area(l, w):
    if l < 0 or w < 0:
        raise ValueError("cannot have negative side lengths")
    return l * w


def perimeter(l, w):
    if l < 0 or w < 0:
        raise ValueError("cannot have negative side lengths")
    return 2 * l + 2 * w


def volume(l, w, h):
    if l < 0 or w < 0 or h < 0:
        raise ValueError("cannot have negative side lengths")
    return l * w * h


def surfaceArea(l, w, h):
    if l < 0 or w < 0 or h < 0:
        raise ValueError("cannot have negative side lengths")
    return 2 * (l * w + l * h + h * w)
