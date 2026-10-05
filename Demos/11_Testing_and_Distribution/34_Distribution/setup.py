
from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="my_bank_package",
    version="0.1.0",
    description="A simple banking application package",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Important for Markdown rendering on PyPI
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_bank_package",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": ["pytest", "flake8"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)

