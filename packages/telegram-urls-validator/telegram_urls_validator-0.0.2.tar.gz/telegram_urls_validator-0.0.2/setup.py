import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'
DESCRIPTION = 'Validator for Telegram URLs.'
LONG_DESCRIPTION = 'A package that allows to validate Telegram urls.'

# Setting up
setup(
    name="telegram_urls_validator",
    version=VERSION,
    author="Emir Takhaviev",
    author_email="tah116emir@outlook.com",
    description=DESCRIPTION,
    packages=find_packages(exclude=["tests*"]),
    keywords=['python', 'telegram urls', 'validation'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
