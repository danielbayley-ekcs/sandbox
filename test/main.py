from main import main


def test_valid():
  assert main("https://ekcsus.github.io/AiAgent/valid.png")

def test_invalid():
  assert main("https://ekcsus.github.io/AiAgent/fake.png") is False
