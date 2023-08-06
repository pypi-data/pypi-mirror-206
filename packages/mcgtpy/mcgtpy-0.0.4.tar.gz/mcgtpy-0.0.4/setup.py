from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'My first Python Package!'
LONG_DESCRIPTION = 'This package will have everything I use on a daily basis to make life easier when coding in Python.'

author_name = "Myles Thomas"
author_email = "mylescgthomas@gmail.com"

setup(
    name="mcgtpy",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=author_name,
    author_email=author_email,
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)