# Custom `cut` Tool

This project is a custom implementation of the Unix `cut` command-line tool. It is designed to extract specific fields from lines of text, adhering to the Unix philosophy of building simple, composable programs that can be connected to create powerful data processing pipelines.

## Features

- Extract specific fields from text files or standard input.
- Support for custom field delimiters.
- Ability to read from standard input when no filename is provided.
- Simple command-line interface.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/custom-cut-tool.git
    cd custom-cut-tool
    ```
2. Make the script executable:
    ```bash
    ```chmod +x ccut.py

# Usage
The ccut tool can be used to extract fields from text files or standard input. Below are some example usages:
1. Extract the second field from a tab-separated file:
    ```bash
    ./ccut.py -f2 sample.tsv
    ```
2. Use a comma as the delimiter and extract the first field:
    ```bash
    ./ccut.py -f1 -d, fourchords.csv
    ```
3. Extract multiple fields (e.g., fields 1 and 2):
    ```bash
    ./ccut.py -f1,2 sample.tsv
    ```
4. Use standard input:
    ```bash
    tail -n5 fourchords.csv | ./ccut.py -d, -f"1 2"
    ```

# Implementation Details
- Field Extraction: The tool uses the -f option to specify which fields to extract. Fields are zero-indexed internally.
- Delimiter: The -d option allows you to specify a custom delimiter. If not provided, a tab character is used by default.
- Standard Input: If no filename is provided, the tool reads from standard input, making it easy to integrate into pipelines.

# Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.
