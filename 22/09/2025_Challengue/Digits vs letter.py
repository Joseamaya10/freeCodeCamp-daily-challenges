def digits_or_letters(s):
    Letters = "abcdefghijklmnñopqrstuvwxyz"
    Digits = "0123456789"
    count_strings = 0
    count_digits = 0
    s_lower = s.lower()
    for string in s_lower:
      if string in Letters:
        count_strings += 1
      elif string in Digits:
        count_digits += 1
      else:
        continue
    if count_strings > count_digits:
        response = "letters"
    elif count_strings < count_digits:
        response = "digits"
    else:
        response = "tie"
    return response
print(digits_or_letters("abc123"))
print(digits_or_letters("a1b2c3d"))
print(digits_or_letters("1a2b3c4"))
print(digits_or_letters("abc123!@#DEF"))
print(digits_or_letters("H3110 W0R1D"))
print(digits_or_letters("P455W0RD"))