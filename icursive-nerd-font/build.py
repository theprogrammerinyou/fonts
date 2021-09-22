#!/usr/bin/env python
"""
iCursive Nerd Font Patcher
"""

import os
import sys
from glob import glob
from platform import system
from shutil import copyfile, move
from subprocess import STDOUT, call

# {{{Initialization
RED = "\033[0;31m"
BRED = "\033[1;31m"
GREEN = "\033[0;32m"
BGREEN = "\033[1;32m"
YELLOW = "\033[0;33m"
BYELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
BBLUE = "\033[1;34m"
NC = "\033[0m"
os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))


# }}}
def general(style, font_path):  # {{{
    """
    general setup for all styles
    """
    os.chdir(".cache")
    if style == "Op":  # {{{
        copyfile(font_path, "./Operator Mono Book Italic.otf")
        # patch ligatures
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching ligatures..." + NC + "\n")
        os.chdir("operator-mono-lig")
        move("../Operator Mono Book Italic.otf",
             "./original/OperatorMono-BookItalic.otf")
        call(["npm", "install"])
        if system() == "Windows":
            os.system(os.path.abspath("build.bat"))
        else:
            call(["sh", "build.sh"])
        copyfile("./build/OperatorMonoLig-BookItalic.otf",
                 "../Operator Mono Book Italic.otf")
        os.chdir("..")
        # patch nerd font symbols
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching nerd font symbols..." + NC + "\n")
        copyfile("Operator Mono Book Italic.otf",
                 "nerd-fonts/Operator Mono Book Italic.otf")
        os.chdir("nerd-fonts")
        call([
            "python", "font-patcher", "--mono", "-w", "-c", "-ext", "ttf",
            r"Operator Mono Book Italic.otf"
        ])
        for file in glob("Operator*Windows Compatible.ttf"):
            move(file, "../Operator Mono Book Italic.ttf")
        os.remove("Operator Mono Book Italic.otf")
        os.remove("../Operator Mono Book Italic.otf")
        os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))
        # }}}
    elif style == "Dk":  # {{{
        copyfile(font_path, "Dank Mono Italic.ttf")
        # patch nerd font symbols
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching nerd font symbols..." + NC + "\n")
        move("Dank Mono Italic.ttf", "nerd-fonts/Dank Mono Italic.ttf")
        os.chdir("nerd-fonts")
        call([
            "python", "font-patcher", "--mono", "-w", "-c", "-ext", "ttf",
            r"Dank Mono Italic.ttf"
        ])
        for file in glob("Dank*Windows Compatible.ttf"):
            move(file, "../Dank Mono Italic.ttf")
        os.remove("Dank Mono Italic.ttf")
        os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))
        # }}}
    elif style == "Cg":  # {{{
        copyfile(font_path, "Cartograph Italic.ttf")
        # patch nerd font symbols
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching nerd font symbols..." + NC + "\n")
        move("Cartograph Italic.ttf", "nerd-fonts/Cartograph Italic.ttf")
        os.chdir("nerd-fonts")
        call([
            "python", "font-patcher", "--mono", "-w", "-c", "-ext", "ttf",
            r"Cartograph Italic.ttf"
        ])
        for file in glob("*artograp*Windows Compatible.ttf"):
            move(file, "../Cartograph Italic.ttf")
        os.remove("Cartograph Italic.ttf")
        os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))
        # }}}


# }}}
def build(style):  # {{{
    """
    build fonts
    """
    dev_null = open(os.devnull, 'w')
    if style == "Op":  # {{{
        # Fira Code iCursive Op
        os.mkdir(os.path.join(os.getcwd(), "Fira Code iCursive Op"))
        copyfile("Fira Code iCursive S12/Fira Code iCursive S12 Regular.ttf",
                 "Fira Code iCursive Op/Fira Code iCursive Op Regular.ttf")
        copyfile("Fira Code iCursive S12/Fira Code iCursive S12 Bold.ttf",
                 "Fira Code iCursive Op/Fira Code iCursive Op Bold.ttf")
        copyfile(".cache/Operator Mono Book Italic.ttf",
                 "Fira Code iCursive Op/Fira Code iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Fira Code iCursive Op",
            r"Fira Code iCursive Op/Fira Code iCursive Op Regular.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Fira Code iCursive Op",
            r"Fira Code iCursive Op/Fira Code iCursive Op Bold.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Fira Code iCursive Op",
            r"Fira Code iCursive Op/Fira Code iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Source Code Pro iCursive Op
        os.mkdir(os.path.join(os.getcwd(), "Source Code Pro iCursive Op"))
        copyfile(
            "Source Code Pro iCursive S12/" +
            "Source Code Pro iCursive S12 Regular.ttf",
            "Source Code Pro iCursive Op/" +
            "Source Code Pro iCursive Op Regular.ttf")
        copyfile(
            "Source Code Pro iCursive S12/" +
            "Source Code Pro iCursive S12 Bold.ttf",
            "Source Code Pro iCursive Op/" +
            "Source Code Pro iCursive Op Bold.ttf")
        copyfile(
            ".cache/Operator Mono Book Italic.ttf",
            "Source Code Pro iCursive Op/" +
            "Source Code Pro iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Source Code Pro iCursive Op", r"Source Code Pro iCursive Op/" +
            r"Source Code Pro iCursive Op Regular.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Source Code Pro iCursive Op", r"Source Code Pro iCursive Op/" +
            r"Source Code Pro iCursive Op Bold.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Source Code Pro iCursive Op", r"Source Code Pro iCursive Op/" +
            r"Source Code Pro iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # InconsolataLGC iCursive Op
        os.mkdir(os.path.join(os.getcwd(), "InconsolataLGC iCursive Op"))
        copyfile(
            "InconsolataLGC iCursive S12/" +
            "InconsolataLGC iCursive S12 Regular.ttf",
            "InconsolataLGC iCursive Op/InconsolataLGC iCursive Op Regular.ttf"
        )
        copyfile(
            "InconsolataLGC iCursive S12/InconsolataLGC iCursive S12 Bold.ttf",
            "InconsolataLGC iCursive Op/InconsolataLGC iCursive Op Bold.ttf")
        copyfile(
            ".cache/Operator Mono Book Italic.ttf",
            "InconsolataLGC iCursive Op/InconsolataLGC iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"InconsolataLGC iCursive Op", r"InconsolataLGC iCursive Op/" +
            r"InconsolataLGC iCursive Op Regular.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"InconsolataLGC iCursive Op",
            r"InconsolataLGC iCursive Op/InconsolataLGC iCursive Op Bold.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"InconsolataLGC iCursive Op",
            r"InconsolataLGC iCursive Op/InconsolataLGC iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Meslo iCursive Op
        os.mkdir(os.path.join(os.getcwd(), "Meslo iCursive Op"))
        copyfile("Meslo iCursive S12/Meslo iCursive S12 Regular.ttf",
                 "Meslo iCursive Op/Meslo iCursive Op Regular.ttf")
        copyfile("Meslo iCursive S12/Meslo iCursive S12 Bold.ttf",
                 "Meslo iCursive Op/Meslo iCursive Op Bold.ttf")
        copyfile(".cache/Operator Mono Book Italic.ttf",
                 "Meslo iCursive Op/Meslo iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py", r"Meslo iCursive Op",
            r"Meslo iCursive Op/Meslo iCursive Op Regular.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py", r"Meslo iCursive Op",
            r"Meslo iCursive Op/Meslo iCursive Op Bold.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py", r"Meslo iCursive Op",
            r"Meslo iCursive Op/Meslo iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Hack iCursive Op
        os.mkdir(os.path.join(os.getcwd(), "Hack iCursive Op"))
        copyfile("Hack iCursive S12/Hack iCursive S12 Regular.ttf",
                 "Hack iCursive Op/Hack iCursive Op Regular.ttf")
        copyfile("Hack iCursive S12/Hack iCursive S12 Bold.ttf",
                 "Hack iCursive Op/Hack iCursive Op Bold.ttf")
        copyfile(".cache/Operator Mono Book Italic.ttf",
                 "Hack iCursive Op/Hack iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py", r"Hack iCursive Op",
            r"Hack iCursive Op/Hack iCursive Op Regular.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py", r"Hack iCursive Op",
            r"Hack iCursive Op/Hack iCursive Op Bold.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py", r"Hack iCursive Op",
            r"Hack iCursive Op/Hack iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Fantasque iCursive Op
        copyfile(".cache/Operator Mono Book Italic.ttf",
                 "Fantasque iCursive Op/Fantasque iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Fantasque iCursive Op",
            r"Fantasque iCursive Op/Fantasque iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Lilex iCursive Op
        os.mkdir(os.path.join(os.getcwd(), "Lilex iCursive Op"))
        copyfile("Lilex iCursive S12/Lilex iCursive S12 Regular.ttf",
                 "Lilex iCursive Op/Lilex iCursive Op Regular.ttf")
        copyfile("Lilex iCursive S12/Lilex iCursive S12 Medium.ttf",
                 "Lilex iCursive Op/Lilex iCursive Op Medium.ttf")
        copyfile("Lilex iCursive S12/Lilex iCursive S12 Bold.ttf",
                 "Lilex iCursive Op/Lilex iCursive Op Bold.ttf")
        copyfile(".cache/Operator Mono Book Italic.ttf",
                 "Lilex iCursive Op/Lilex iCursive Op Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Lilex iCursive Op",
            r"Lilex iCursive Op/Lilex iCursive Op Regular.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Lilex iCursive Op",
            r"Lilex iCursive Op/Lilex iCursive Op Medium.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Lilex iCursive Op",
            r"Lilex iCursive Op/Lilex iCursive Op Bold.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Lilex iCursive Op",
            r"Lilex iCursive Op/Lilex iCursive Op Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # }}}
    elif style == "Dk":  # {{{
        # Fantasque iCursive Dk
        copyfile(".cache/Dank Mono Italic.ttf",
                 "Fantasque iCursive Dk/Fantasque iCursive Dk Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Fantasque iCursive Dk",
            r"Fantasque iCursive Dk/Fantasque iCursive Dk Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Lilex iCursive Dk
        copyfile(".cache/Dank Mono Italic.ttf",
                 "Lilex iCursive Dk/Lilex iCursive Dk Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Lilex iCursive Dk",
            r"Lilex iCursive Dk/Lilex iCursive Dk Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Cascadia Code iCursive Dk
        copyfile(".cache/Dank Mono Italic.ttf",
                 "Cascadia Code iCursive Dk/Cascadia Code iCursive Dk Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Cascadia Code iCursive Dk",
            r"Cascadia Code iCursive Dk/Cascadia Code iCursive Dk Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # }}}
    elif style == "Cg":  # {{{
        # Cascadia Code iCursive Cg
        copyfile(
            ".cache/Cartograph Italic.ttf", "Cascadia Code iCursive Cg/" +
            "Cascadia Code iCursive Cg Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Cascadia Code iCursive Cg",
            r"Cascadia Code iCursive Cg/Cascadia Code iCursive Cg Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # Recursive Code iCursive Cg
        copyfile(
            ".cache/Cartograph Italic.ttf", "Recursive Code iCursive Cg/" +
            "Recursive Code iCursive Cg Italic.ttf")
        call([
            "python", ".cache/fontname.py/fontname.py",
            r"Recursive Code iCursive Cg",
            r"Recursive Code iCursive Cg/Recursive Code iCursive Cg Italic.ttf"
        ],
             stdout=dev_null,
             stderr=STDOUT)
        # }}}


# }}}
if len(sys.argv) != 3:
    print("\n" + BYELLOW + "==>" + NC + " " + BRED + "Invalid arguments." +
          NC + "\n")
    sys.exit(1)
elif sys.argv[1] != "Op" and sys.argv[1] != "Dk" and sys.argv[1] != "Cg":
    print("\n" + BYELLOW + "==>" + NC + " " + BRED + "Invalid arguments." +
          NC + "\n")
    sys.exit(1)
elif not os.path.isfile(sys.argv[2]):
    print("\n" + BYELLOW + "==>" + NC + " " + BRED + "File not accessible." +
          NC + "\n")
    sys.exit(1)
else:
    general(sys.argv[1], sys.argv[2])
    build(sys.argv[1])
print("\n" + BYELLOW + "==>" + NC + " " + BBLUE + "Cache directory:" + NC +
      GREEN + os.path.join(os.getcwd(), ".cache") + "\n")
CLEAN = input(BYELLOW + "==>" + NC + " " + BBLUE + "Clean cache? [Y/n] ")
if CLEAN in ("", "Y", "y"):
    print(BYELLOW + "==>" + NC + " " + BGREEN +
          "git clean -fdx -- .cache" + NC + "\n")
    call(["git", "clean", "-d", "-f", "-x", "--", ".cache"])
print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
      "Done." + NC + "\n")
