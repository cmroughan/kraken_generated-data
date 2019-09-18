# Three tools for text preparation

Written by Christine Roughan. Feel free to use and adapt if you find them useful.

## 1) `count_chars.py`

A diagnostic tool that outputs a list of characters that are present in an input text as well as a count of those characters. Expects a .txt file as input.

Usage in the terminal:

`python count_chars.py <txt_file>`

## 2) `remove_chars.py`

A tool which will remove the desired characters from an input text.

Usage in the terminal:

`python remove_chars.py -i <input txt> -o <output txt> <characters>`

The input must be a .txt file. Output is optional and defaults to out.txt. If multiple characters are desired to be removed, separate each character with a space. Unicode escape codes may be used for characters if desired.

E.g.: `python remove_chars.py -i text.txt a b c \u0064`

## 3) `line_breaks.py`

A tool which will take an input .txt file and split each paragraph into lines based on a specified character length. (Do not use a .txt file which has already been split into lines.) The default character length is 65 characters, but this may be changed with the `-c` option. The default output text is out_lines.txt.

Usage in the terminal:

`python line_breaks.py -c <character_length> -o <output txt> <input txt>`
