# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
from pathlib import Path
import os

os.chdir('tmp')
sourcePath = Path(os.getcwd())
print(sourcePath)

filename = 'file-to-move'
print(filename)

fullSourcePath = sourcePath / filename

print(fullSourcePath)
print('[INFO] Deleting ' + str(fullSourcePath))
# Removes file or symlink
Path.unlink(fullSourcePath)
