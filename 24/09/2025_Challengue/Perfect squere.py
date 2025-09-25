import math
def is_perfect_square(n):
    try:
      squere = int(math.sqrt(n))
      if squere**2 == n:
        return True
      else:
        return False
    except:
        return False
print(is_perfect_square(9))
print(is_perfect_square(49))
print(is_perfect_square(1))
print(is_perfect_square(2))
print(is_perfect_square(99))
print(is_perfect_square(-9))
print(is_perfect_square(0))
print(is_perfect_square(25281))