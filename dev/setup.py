import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "File Engine",
    version = "1.3",
    description = "File management & automation tool",
    author = "OfficialAhmed0",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
