#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from ansi2html import Ansi2HTMLConverter

# Global converter
conv = Ansi2HTMLConverter()

def RandomString(fdp, min_len, max_len):
  str_len = fdp.ConsumeIntInRange(min_len, max_len)
  return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    ansi = RandomString(fdp, 0, 20)
    conv.convert(ansi)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()