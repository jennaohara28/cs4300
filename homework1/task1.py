def printing():
    print("Hello, World!")

def test_hello(capsys):
    printing()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"