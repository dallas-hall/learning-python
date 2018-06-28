import shutil

sourcePath = '/home/dhall/dev/python/Automate The Boring Stuff/Chapter08-File IO/tmp'
targetPath = '/home/dhall/dev/python/Automate The Boring Stuff/Chapter09-Organising Files/tmp'

shutil.copytree(sourcePath, targetPath + '/complete-copy/')