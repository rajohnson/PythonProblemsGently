from collections import Counter
from typing import Sequence


def mode(values: Sequence[float]) -> float | None:
    if len(values) == 0:
        return None

    counted_values = Counter(values)

    # Counter.most_common returns sequence(value, count), only want value from index 0
    most_common = counted_values.most_common(1)[0][0]
    return most_common
