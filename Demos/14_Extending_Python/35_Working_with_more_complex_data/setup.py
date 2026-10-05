from setuptools import setup, Extension

setup(
    name="complexdatamodule",
    ext_modules=[Extension("complexdatamodule", ["complexdatamodule.c"])]
)