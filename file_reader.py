# File Reader.

from pathlib import Path

path = Path(‘') # Enter the name of the file.
contents = path.read_text()
print(contents)
