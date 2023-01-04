import hello


def test_hello(capsys):
    hello.hello()
    output = capsys.readouterr().out
    assert output == "Hello, world!\n"
