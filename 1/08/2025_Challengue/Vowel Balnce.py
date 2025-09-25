def is_balanced(s):
    vowels = "aeiouAEIOU"
    length = len(s)
    mid = length // 2

    if length % 2 != 0:
        first_half = s[:mid]
        second_half = s[mid+1:]
    else:
        first_half = s[:mid]
        second_half = s[mid:]

    first_half_vowel_count = sum(1 for char in first_half if char in vowels)
    second_half_vowel_count = sum(1 for char in second_half if char in vowels)

    return first_half_vowel_count == second_half_vowel_count

print(is_balanced("racecar"))
print(is_balanced("Lorem Ipsum"))
print(is_balanced("Kitty Ipsum"))
print(is_balanced("string"))
print(is_balanced(" "))
print(is_balanced("abcdefghijklmnopqrstuvwxyz"))
print(is_balanced("123A#b!E&*456-o.U"))