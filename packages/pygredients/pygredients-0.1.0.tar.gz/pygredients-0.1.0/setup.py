from setuptools import setup, find_packages

setup(
    name='pygredients',
    version='0.1.0',
    description='Pygredients is a Python library for data structures and algorithms.',
    author='François Boulay-Handfield',
    author_email="fbhworks@icloud.com",
    url="https://github.com/FBH514/pygredients",
    license="MIT",
    install_requires=[
        "twine>=4.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="data structures algorithms",
    python_requires=">=3.9"
)