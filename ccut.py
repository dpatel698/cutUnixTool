# Custom Unix-style cut command line tool
import sys
import re


def get_options_dict():
    """
    Assembles all options after ccut command into a dictionary
    :return: dictionary of all options in the command
    """
    file_pattern = r"^[^/\\]+\.[^/\\]+$"
    opts = {}
    for o in sys.argv[1:]:
        if "-f" in o:
            opts["-f"] = [int(_) for _ in o[2:].strip("\"").split(" ")]
        elif "-d" in 0:
            opts["-d"] = o[2:]
        elif re.match(file_pattern, o):
            opts["filename"] = o
        else:
            opts["invalid_option"] = o
            return opts

    return opts


def process_fields(text, delimiter):
    pass


def process_options():
    options_dict = get_options_dict()

    if "invalid_option" in options_dict:
        option = options_dict["invalid_option"]
        print(f"ccut: unknown option {option}")
    if "filename" not in options_dict:
        text = sys.stdin.read()
    else:
        try:
            filename = options_dict["filename"]
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"ccut: {filename}: No such file or directory")
            sys.exit(1)

    delimiter = options_dict["-d"]
    process_fields(text, delimiter)

if __name__ == "__main__":

