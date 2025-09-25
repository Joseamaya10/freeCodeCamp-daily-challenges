import re

def is_mirror(str1, str2):
    filtered_str1 = re.sub(r'[^a-zA-Z]', '', str1)
    filtered_str2 = re.sub(r'[^a-zA-Z]', '', str2)

    return filtered_str1[::-1] == filtered_str2

# Test cases
print(is_mirror("helloworld", "helloworld"))
print(is_mirror("Hello World", "dlroW olleH"))
print(is_mirror("RaceCar", "raCecaR"))
print(is_mirror("RaceCar", "RaceCar"))
print(is_mirror("Mirror", "rorrim"))
print(is_mirror("Hello World", "dlroW-olleH"))
print(is_mirror("Hello World", "!dlroW !olleH"))
