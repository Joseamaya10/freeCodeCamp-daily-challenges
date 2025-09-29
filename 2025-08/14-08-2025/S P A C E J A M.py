import re
def space_jam(s):
    x = re.findall(r'\S', s)
    return "  ".join(x).upper()
print(space_jam("Hello World?!"))
print(space_jam("freeCodeCamp"))
