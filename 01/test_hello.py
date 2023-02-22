import hello
import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize("name", ("Alice", "Bob", "Carl"))
def test_hello(
    capsys: CaptureFixture[str], monkeypatch: MonkeyPatch, name: str
) -> None:
    def mock_input(prompt: str) -> str:
        print(prompt, end="")
        print(name)
        return name

    monkeypatch.setattr("builtins.input", mock_input)
    hello.hello()
    output = capsys.readouterr().out
    assert output == f"Hello, world!\nWhat is your name?\n{name}\nHello, {name}.\n"
