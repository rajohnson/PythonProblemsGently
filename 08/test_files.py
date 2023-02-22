from pathlib import Path

from files import appendToFile, readFromFile, writeToFile


def test_write_append_read(tmp_path: Path) -> None:
    filename = tmp_path / "greet.txt"
    writeToFile(filename, "Hello!\n")
    appendToFile(filename, "Goodbye!\n")
    expected = "Hello!\n" + "Goodbye!\n"
    assert readFromFile(filename) == expected
