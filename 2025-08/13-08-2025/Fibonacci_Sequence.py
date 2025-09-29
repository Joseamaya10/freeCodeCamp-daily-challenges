def fibonacci_sequence(start_sequence, length):
    counter = 0
    sequence = list()
    if length >= 3:
        while counter < length - 2:
            last = start_sequence[-2] + start_sequence[-1]
            start_sequence.append(last)
            counter += 1
        return start_sequence
    elif length < 3:
        for i in range(0, length):
            sequence.append(start_sequence[i])
        return sequence
print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))