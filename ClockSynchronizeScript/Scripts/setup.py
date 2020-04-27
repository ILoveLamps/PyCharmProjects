import sys
from cx_Freeze import setup, Executable
from multiprocessing import Queue

base = None

# Necessary for 32-bit systems
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("ClockSync.py", base=base, targetName="ClockSync.exe")]

# Any packages that need to be added for compilation.
packages = ["multiprocessing", "pynput", "time"]

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    # EXE NAME HERE
    name="ClockSync",
    options=options,
    version="0.1",
    description='Synchronizes windows clock',
    executables=executables
)
