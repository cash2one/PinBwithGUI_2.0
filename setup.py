__author__ = 'xuhuan'
# !encoding:utf-8
# python setup.py build
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Console"
setup(
    name="pinbiao",
    version="0.1",
    description="Pinbiao",
    executables=[Executable("test.py", base=base, icon='image/icon.ico')]
    )