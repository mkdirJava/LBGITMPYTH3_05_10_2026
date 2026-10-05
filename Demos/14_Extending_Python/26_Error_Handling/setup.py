from setuptools import setup, Extension

setup(
    name="filesavemodule",
    ext_modules=[Extension("filesavemodule", ["filesavemodule.c"])]
)