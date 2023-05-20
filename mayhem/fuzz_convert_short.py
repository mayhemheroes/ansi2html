#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from ansi2html import Ansi2HTMLConverter

# Global converter
conv = Ansi2HTMLConverter()

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    ansi = fdp.ConsumeUnicodeNoSurrogates(20)
    conv.convert(ansi)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()