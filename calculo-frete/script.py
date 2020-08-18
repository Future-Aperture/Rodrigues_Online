from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("main.py", base=base)]

packages = ["functions"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Afton",
    options = options,
    version = "1.0",
    description = '',
    executables = executables
)