def set_bat():
    with open("upload.bat", "w") as w:
        w.write("""python setup.py sdist bdist_wheel
python -m twine upload dist/*
python clean_update.py
""")


def set_clean_update():
    with open("clean_update.py", "w") as w:
        w.write("""import shutil
import os
from rich.console import Console
from rich.progress import track

console = Console()


def main():
    with console.status("Find the full path of .egg-info folder"):
        egg_info: list = []
        for file in os.listdir():
            if file.endswith(".egg-info"):
                egg_info.append(file)
                console.print(file)
    for file in track(["build", "dist", "logs", *egg_info], description="Deleting files"):
        if os.path.isdir(file) and os.access(file, os.W_OK):
            shutil.rmtree(file)


if __name__ == "__main__":
    main()
""")


def set_setup():
    with open("setup.py", "w") as w:
        w.write("""# -*- coding: utf-8 -*-
import setuptools
import Musicreater

with open("requirements.txt", "r", encoding="utf-8") as fh:
    dependences = fh.read().strip().split("\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read().replace(
        "./docs/", "https://github.com/TriM-Organization/Musicreater/blob/master/docs/"
    )

setuptools.setup(
    name="Musicreater",
    version=Musicreater.__version__,
    author="Eilles Wan, bgArray",
    author_email="TriM-Organization@hotmail.com",
    description="一款免费开源的 《我的世界》 mid音乐转换库。\n"
    "A free open-source python library used to convert midi into Minecraft.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TriM-Organization/Musicreater",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Chinese (Simplified)",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # 需要安装的依赖
    install_requires=dependences,
)
""")


def set_requirements():
    with open("requirements.txt", "w") as w:
        w.write("""Brotli>=1.0.9
mido>=1.2.10""")


def set_main():
    set_bat()
    set_clean_update()
    set_setup()
    set_requirements()
