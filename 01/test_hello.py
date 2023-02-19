import pytest
import hello


@pytest.mark.parametrize("name", ("Alice", "Bob", "Carl"))
def test_hello(capsys, monkeypatch, name):
    def mock_input(prompt):
        print(prompt, end="")
        print(name)
        return name

    monkeypatch.setattr("builtins.input", mock_input)
    hello.hello()
    output = capsys.readouterr().out
    assert output == f"Hello, world!\nWhat is your name?\n{name}\nHello, {name}.\n"
