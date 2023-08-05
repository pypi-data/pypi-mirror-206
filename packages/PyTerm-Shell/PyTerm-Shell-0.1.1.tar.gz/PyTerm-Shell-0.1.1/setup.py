from setuptools import setup, find_packages
from io import open
from os import path



setup (
 name = 'PyTerm-Shell',
 description = 'Making an aesthetic minimalist Linux shell in Python',
 version = '0.1.01',
 python_requires='>=3.7',
 entry_points = {
        'console_scripts': ['PyTerm=PyTerm.cli_assist:main'],
 },
 include_package_data=True,
 author="Nick Tsiones",
 license='MIT',
 url='https://github.com/MetalKamina/PyTerm',
  author_email='ntsiones@gmail.com',
  classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)