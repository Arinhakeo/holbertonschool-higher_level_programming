#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Attempt to print the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Handle cases where value is not an integer
        return False
