from setuptools import Extension, setup

setup(
    name="finance",
    version="1.0.0",
    description="Finance C extension for Python",
    ext_modules=[Extension("finance", ["EG14_Solution_finance_module.c"])],
)