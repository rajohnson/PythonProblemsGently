import geometry
import pytest


@pytest.mark.parametrize(
    "length, width, area", [(4, 10, 40), (0, 9999, 0), (10, 10, 100), (5, 8, 40)]
)
def test_area(length: float, width: float, area: float) -> None:
    assert geometry.area(length, width) == area


@pytest.mark.parametrize(
    "length, width",
    [
        (-1, 1),
        (1, -1),
    ],
)
def test_area_negative(length: float, width: float) -> None:
    with pytest.raises(ValueError):
        geometry.area(length, width)


@pytest.mark.parametrize(
    "length, width, perimeter",
    [(4, 10, 28), (0, 9999, 19998), (10, 10, 40), (5, 8, 26)],
)
def test_perimeter(length: float, width: float, perimeter: float) -> None:
    assert geometry.perimeter(length, width) == perimeter


@pytest.mark.parametrize(
    "length, width",
    [
        (-1, 1),
        (1, -1),
    ],
)
def test_perimeter_negative(length: float, width: float) -> None:
    with pytest.raises(ValueError):
        geometry.perimeter(length, width)


@pytest.mark.parametrize(
    "length, width, height, volume",
    [(10, 4, 5, 200), (10, 10, 10, 1000), (9999, 0, 9999, 0), (5, 8, 10, 400)],
)
def test_volume(length: float, width: float, height: float, volume: float) -> None:
    assert geometry.volume(length, width, height) == volume


@pytest.mark.parametrize(
    "length, width, height",
    [
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
        (-1, -1, 1),
        (-1, 1, -1),
        (1, -1, -1),
        (-1, -1, -1),
    ],
)
def test_volume_negative(length: float, width: float, height: float) -> None:
    with pytest.raises(ValueError):
        geometry.volume(length, width, height)


@pytest.mark.parametrize(
    "length, width, height, surface_area",
    [
        (10, 4, 5, 220),
        (10, 10, 10, 600),
        (9999, 0, 9999, 199960002),
        (5, 8, 10, 340),
    ],
)
def test_surface_area(
    length: float, width: float, height: float, surface_area: float
) -> None:
    assert geometry.surfaceArea(length, width, height) == surface_area


@pytest.mark.parametrize(
    "length, width, height",
    [
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
        (-1, -1, 1),
        (-1, 1, -1),
        (1, -1, -1),
        (-1, -1, -1),
    ],
)
def test_surface_area_negative(length: float, width: float, height: float) -> None:
    with pytest.raises(ValueError):
        geometry.surfaceArea(length, width, height)
