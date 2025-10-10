def jbelmu(text):
    text_list = text.split()
    lst = []
    lista0 = []
    lista = []
    for word in text_list:
        if len(word) > 3:
            lst.append(word)
            counter = 0
            while counter < len(lst):
              for letter in lst[counter][1:-1]:
                lista.append(letter)
              lista.sort()
              lista1 = lst[counter][0] + "".join(lista) + lst[counter][-1]
              lista = []
              counter += 1
            lista0.append(lista1)
        else: 
          lista0.append(word)
    return " ".join(lista0)
print(jbelmu("freecodecamp"))
print(jbelmu("the quick brown fox jumps over the lazy dog"))