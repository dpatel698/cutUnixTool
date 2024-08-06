#!/usr/bin/env python
# Custom Unix-style cut command line tool
import sys
import locale

local_encoding = locale.getpreferredencoding()
default_delimeter = "\t"


def get_options_dict():
    """
    Assembles all options after ccut command into a dictionary
    :return: dictionary of all options in the command
    """
    opts = dict()
    opts["filename"] = sys.argv[-1]
    opts["-d"] = default_delimeter

    for o in sys.argv[1:]:
        if "-f" in o:
            field_delimiter = ""
            for char in o:
                if not char.isalnum() and char not in ["\""]:
                    field_delimiter = char
            opts["-f"] = [int(_) - 1 for _ in o[2:].strip("\"").split(field_delimiter)]
        elif "-d" in o:
            opts["-d"] = o[2:]
        elif "-" == o:
            if "filename" in opts:
                del opts["filename"]
        elif "-" != o and "-" == o[0]:
            opts["invalid_option"] = o
            return opts
    if "filename" in opts and opts["filename"][0] == "-":
        del opts["filename"]

    return opts


def check_incorrect_options(options_dict):
    if "invalid_option" in options_dict:
        option = options_dict["invalid_option"]
        print(f"ccut: unknown option {option}")
        sys.exit(1)
    if "-f" not in options_dict:
        print("ccut: -f missing")
        sys.exit(1)


def process_fields(text, fields, delimiter):
    for line in text.split("\n"):
        row = line.split(delimiter)
        row_fields = f"{delimiter}".join(col for col in [row[i] for i in fields])
        print(row_fields)


def process_options():
    options_dict = get_options_dict()
    check_incorrect_options(options_dict)

    if "filename" not in options_dict:
        text = sys.stdin.read()
    else:
        try:
            filename = options_dict["filename"]
            with open(filename, 'r', encoding=local_encoding) as file:
                text = file.read()
        except FileNotFoundError:
            print(f"ccut: {filename}: No such file or directory")
            sys.exit(1)

    delimiter = options_dict["-d"]
    process_fields(text, options_dict["-f"], delimiter)


def main():
    if len(sys.argv) < 2:
        print("Usage: ccut -f... [-d] [file] [-]")
        sys.exit(1)
    else:
        process_options()
        sys.exit(0)


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    main()

