import os

# This will return usr/bin on Linux and usr\\bin on Windows. The \ needs to be escaped to become a literal \, so \\ is needed.
path = os.path.join('usr', 'bin')
print(path)
