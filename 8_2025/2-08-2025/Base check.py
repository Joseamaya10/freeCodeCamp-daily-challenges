import re

def is_valid_number(n, base):
    string = n.upper()

    if base == 2:
        if re.search(r'[^01]', string):
            return False
        else:
            return True
    elif base == 8:
        if re.search(r'[^0-7]', string):
            return False
        else:
            return True
    elif base == 10:
        if re.search(r'[^0-9]', string):
            return False
        else:
            return True
    elif base == 16:
        if re.search(r'[^0-9A-F]', string):
            return False
        else:
            return True
    elif base == 36:
        if re.search(r'[^0-9A-Z]', string):
            return False
        else:
            return True
    else:
        return True

print(is_valid_number("10101", 2))
print(is_valid_number("10201", 2))