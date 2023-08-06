from pathlib import Path
from setuptools import setup

long_description = (Path(__file__).parent / "README.md").read_text('utf-8').split('# Installation')[0]

setup(
    name="manga-ocr-abang",
    version='0.2.0',
    description="OCR for Japanese manga",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbangTanYiHan/manga-ocr-abang",
    author="Abang",
    author_email="shinichiconan1997@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=['manga_ocr'],
    include_package_data=True,
    install_requires=[
        "fire",
        "fugashi",
        "jaconv",
        "loguru",
        "numpy",
        "Pillow",
        "pyperclip",
        "sentencepiece",
        "torch>=1.0",
        "transformers>=4.12.5",
        "unidic_lite",
    ],
    entry_points={
        "console_scripts": [
            "manga_ocr=manga_ocr.__main__:main",
        ]
    },
)
