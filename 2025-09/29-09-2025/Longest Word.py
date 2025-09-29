import re
def get_longest_word(sentence):
    x = re.findall(r'[a-zA-Z]+', sentence)
    length = None
    word = ""
    for i in x:
        if length is None or len(i) > length:
            length = len(i)
        else:
            continue
    for i in x:
        if len(i) == length:
            word += i
            break
    return word
print(get_longest_word("coding is fun"))
print(get_longest_word("Coding challenges are fun and educational."))
print(get_longest_word("This sentence has multiple long words."))