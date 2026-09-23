"""
File: hello_tuna_fish.py
Author: Samatar Ali Abdullahi
Description: This program is a python program displaying a basic hello world message and variations.

References:
[1] “platform — Access to underlying platform’s identifying data — Python 3.9.7 documentation,” docs.python.org. https://docs.python.org/3/library/platform.html (accessed Sept. 14, 2026).
[2] “ChatGPT,” ChatGPT, 2026. https://chatgpt.com/c/6aa5ce2f-b868-83e9-bd28-4a355553dc60 (accessed Sept. 14, 2026).
[3] G. van Rossum, B. Warsaw, and N. Coghlan, “PEP 8 – Style Guide for Python Code,” peps.python.org, July 05, 2001. https://peps.python.org/pep-0008/ (accessed Sept. 14, 2026).
"""

import platform


def display_program_information():
    """This function displays simple hello world and Python statements, and author name that will then be printed to the console."""
    print("Hello Tuna Fish!")
    print("Python")
    platform.python_version
    print("Samatar Ali Abdullahi")


def main():
    display_program_information()
    """This function calls the main function in order to complete the specifics and using the method.
    """

if __name__ == "__main__":
    main()