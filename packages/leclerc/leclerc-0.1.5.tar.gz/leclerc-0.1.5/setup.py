import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "leclerc",
    version = "0.1.5",
    author = "Luke Marhsall and Hoshang Mehta",
    author_email = "luke.marshall@suncable.energy",
    description = ("Leclerc conducts a montecarlo analysis on a range of function files that involve formula derivation"),
    license = "Open Source",
    keywords = "Montecarlo, levelised cost",
    url = "https://pypi.org/project/leclerc/",
    packages=['leclerc'],
        long_description_content_type="text/markdown",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)