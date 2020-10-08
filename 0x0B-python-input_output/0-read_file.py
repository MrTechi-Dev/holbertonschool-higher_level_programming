nes (6 sloc) 177 Bytes
#!/usr/bin/python3
"""create"""


def read_file(filename=""):
    """reading a file"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
