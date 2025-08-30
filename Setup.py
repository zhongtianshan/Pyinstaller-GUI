#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

REQUIRES = ["PySide6", "PyInstaller"]


def install(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])


def main():
    for module in REQUIRES:
        install(module)


if __name__ == "__main__":
    main()