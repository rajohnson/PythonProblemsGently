import pytest
from chess_color import getChessSquareColor


@pytest.mark.parametrize("row, col", [(0, 1), (0, 5), (0, 7), (7, 6)])
def test_chess_black(row, col):
    assert getChessSquareColor(row, col) == "black"


@pytest.mark.parametrize("row, col", [(0, 0), (7, 1), (7, 7)])
def test_chess_white(row, col):
    assert getChessSquareColor(row, col) == "white"


@pytest.mark.parametrize(
    "row, col", [(0, 9), (0, 8), (0, -1), (-1, 5), (8, 5)]
)
def test_chess_bad_square(row, col):
    assert getChessSquareColor(row, col) == ""
