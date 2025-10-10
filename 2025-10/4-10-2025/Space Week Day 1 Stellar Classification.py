''' "O": 30,000 K or higher

"B": 10,000 K - 29,999 K

"A": 7,500 K - 9,999 K

"F": 6,000 K - 7,499 K

"G": 5,200 K - 5,999 K

"K": 3,700 K - 5,199 K

"M": 0 K - 3,699 K'''
def classification(temp):
    if temp >= 30000:
        return "O"
    elif temp in range(10000, 30000):
        return "B"
    elif temp in range(7500, 10000):
        return "A"
    elif temp in range(6000, 7500):
        return "F"
    elif temp in range(5200, 6000):
        return "G"
    elif temp in range(3700, 5200):
        return "K"
    elif temp in range(0, 3700):
        return "M"
    
print(classification(29999))
print(classification(9999))
print(classification(210000))