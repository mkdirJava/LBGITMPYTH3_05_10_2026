from setuptools import setup, Extension

setup(
    name="bankmodule",
    ext_modules=[Extension("bankmodule", ["bankmodule.c"])]
)