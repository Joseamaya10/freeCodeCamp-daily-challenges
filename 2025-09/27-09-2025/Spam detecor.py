import re
def is_spam(number):
    special_characters = "+ ()-"
    x = number.split()
    A = x[0]
    BBB = x[1]
    third = x[2].split("-")
    CCC = third[0]
    DDDD = third[1]
    if A[1] != "0" or len(A) > 3:
        first_test = True
    else:
        first_test = False
    b = re.findall(r'\d+', BBB)
    bbb = int(b[0])
    if bbb < 200 or bbb > 900:
        second_test = True
    else:
        second_test = False
    if str(int(CCC[0]) + int(CCC[1]) + int(CCC[2])) in DDDD:
        third_test = True
    else:
        third_test = False
    clean = list()
    for n in number:
        if not n in special_characters:
            clean.append(n)
    counter = 0
    fourth_test = False
    while counter < (len(clean) - 3):
        if clean[counter] == clean[counter+1] and clean[counter] == clean[counter+2] and clean[counter] == clean[counter+3]:
            fourth_test = True
            break
        counter += 1
    if first_test or second_test or third_test or fourth_test:
        return True
    else:
        return False
print(is_spam("+0 (200) 234-0182"))
print(is_spam("+091 (555) 309-1922"))
print(is_spam("+1 (555) 435-4792"))
print(is_spam("+0 (955) 234-4364"))
print(is_spam("+0 (155) 131-6943"))
print(is_spam("+0 (555) 135-0192"))
print(is_spam("+0 (555) 564-1987"))
print(is_spam("+00 (555) 234-0182"))
