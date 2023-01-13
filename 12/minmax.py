from typing import Sequence, Optional


def getSmallest(values: Sequence[int]) -> Optional[int]:
    if not values:
        return None
    smallest = values[0]
    for v in values:
        if v < smallest:
            smallest = v
    return smallest


if __name__ == "__main__":
    print(f"{getSmallest([1,2,3])=}")
    print(f"{getSmallest([3,2,1])=}")