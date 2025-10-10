def to_binary(n):
    if n == 0:
        return "0"
    
    binary_string = ""
    while n > 0:
        remainder = n % 2
        binary_string = str(remainder) + binary_string
        n = n // 2
    return binary_string
print(to_binary(5))