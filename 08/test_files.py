from files import writeToFile, appendToFile, readFromFile


def test_write_append_read(tmp_path):
    filename = tmp_path / "greet.txt"
    writeToFile(filename, "Hello!\n")
    appendToFile(filename, "Goodbye!\n")
    expected = "Hello!\n" + "Goodbye!\n"
    assert readFromFile(filename) == expected
