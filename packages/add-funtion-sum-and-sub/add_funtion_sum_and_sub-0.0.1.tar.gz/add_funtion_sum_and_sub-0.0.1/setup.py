from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'add_funtion_sum_and_sub'
LONG_DESCRIPTION = 'A package to perform arithmetic operations'

# Setting up
setup(
    name="add_funtion_sum_and_sub",
    version=VERSION,
    author="kurban hussain",
    author_email="kurbanhussain086@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'math', 'mathematics', 'python tutorial', 'kurban hussain','two number add module','sum','sub','number'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)