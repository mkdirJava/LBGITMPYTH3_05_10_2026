from setuptools import setup, Extension

setup(
    name="myminimalmodule",
    ext_modules=[Extension("myminimalmodule", ["myminimalmodule.c"])]
)