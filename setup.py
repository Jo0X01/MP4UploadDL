from setuptools import setup, find_packages

__author__ = "Jo0x01"
__pkg_name__ = "MP4UploadDL"
__version__ = "1.0.0"
__desc__ = """A Python script to download videos from **MP4Upload** using the free download method without waiting."""

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.readlines()

setup(
    name=__pkg_name__,
    version=__version__,
    packages=[__pkg_name__],
    license='MIT',
    description=__desc__,
    author=__author__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jo0x01/MP4UploadDL",
    packages=find_packages(exclude=("tests",)),
    py_modules=["MP4UploadDL"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "mp4upload-dl=MP4UploadDL:main",
            "mp4up-dl=MP4UploadDL:main",
            "MP4UploadDL=MP4UploadDL:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Video",
    ],
    python_requires=">=3.2",
)
