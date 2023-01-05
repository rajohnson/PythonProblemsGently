import pytest
import geometry


@pytest.mark.parametrize(
    "l, w, area", [(4, 10, 40), (0, 9999, 0), (10, 10, 100), (5, 8, 40)]
)
def test_area(l, w, area):
    assert geometry.area(l, w) == area


@pytest.mark.parametrize(
    "l, w, perimeter",
    [(4, 10, 28), (0, 9999, 19998), (10, 10, 40), (5, 8, 26)],
)
def test_perimeter(l, w, perimeter):
    assert geometry.perimeter(l, w) == perimeter


@pytest.mark.parametrize(
    "l, w,h, volume",
    [(10, 4, 5, 200), (10, 10, 10, 1000), (9999, 0, 9999, 0), (5, 8, 10, 400)],
)
def test_volume(l, w, h, volume):
    assert geometry.volume(l, w, h) == volume


@pytest.mark.parametrize(
    "l, w,h, surface_area",
    [
        (10, 4, 5, 220),
        (10, 10, 10, 600),
        (9999, 0, 9999, 199960002),
        (5, 8, 10, 340),
    ],
)
def test_surface_area(l, w, h, surface_area):
    assert geometry.surfaceArea(l, w, h) == surface_area
