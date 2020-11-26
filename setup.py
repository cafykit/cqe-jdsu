import os
import setuptools

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "cqe-jdsu",
    version = "0.0.1",
    author = "Manali Gupta",
    author_email = "manligup@cisco.com",
    description = ("JDSU OntRemote Libraries. Content is copyright of VIAVI Solutions Inc"
                                   "This is just a pip version of the same"),
    license = "BSD",
    keywords = "JDSU OntRemote Five-g",
    url = "http://packages.python.org/cqe-jdsu",
    packages=setuptools.find_packages(),
    long_description=read('README'),
    scripts=['jdsu/phys_layer.py'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
