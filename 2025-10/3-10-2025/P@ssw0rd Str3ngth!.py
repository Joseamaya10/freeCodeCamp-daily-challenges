import re
def check_strength(password):
    tests = []
    if len(password) >= 8:
        tests.append(True)
    else:
        tests.append(False)
    upper = re.findall('[A-Z]+', password)
    lower = re.findall(r'[a-z]+', password)
    if upper and lower:
        tests.append(True)
    else:
        tests.append(False)
    number = re.findall(r'[0-9]+', password)
    if number:
        tests.append(True)
    else:
        tests.append(False)
    specials = re.findall(r'[!@#$%^&*]+', password)
    if specials:
        tests.append(True)
    else:
        tests.append(False)
    test = 0
    for i in tests:
        if i:
            test += 1
    print(test)
    if test < 2:
        return "weak"
    elif test >= 2 and test < 4:
        return "medium"
    elif test == 4:
        return "strong"
print(check_strength("PASSWORD!"))
print(check_strength("S3cur3P@ssw0rd"))
