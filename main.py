import sys
from urllib.request import urlopen

import magic


def main(url: str) -> bool:
  bytes = urlopen(url).read(16)
  mime_type = magic.from_buffer(bytes, mime=True)
  valid = mime_type == "image/png"
  print(valid)
  return valid


if __name__ == "__main__": main(sys.argv[1])
