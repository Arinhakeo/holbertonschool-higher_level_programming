#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print()
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
