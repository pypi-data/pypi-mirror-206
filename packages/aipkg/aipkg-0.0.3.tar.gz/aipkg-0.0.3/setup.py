from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Streaming video data via networks'


# Setting up
setup(
    name="aipkg",
    version=VERSION,
    author="YB03",
    author_email="<hello@yahoo.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'ai', 'pkg'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
