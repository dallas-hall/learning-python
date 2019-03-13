# https://stackoverflow.com/a/67692
import importlib.util
spec = importlib.util.spec_from_file_location("myCats", "/home/dhall/dev/python/Automate The Boring Stuff/Chapter08-File IO/myCats.py")
myCats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(myCats)

print(myCats.cats)
