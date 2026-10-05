from setuptools import setup, Extension

setup(
    name="mymathsmodule",
    ext_modules=[Extension("mymathsmodule", ["mymathsmodule.c"])]
)