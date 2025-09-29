def second_largest(arr):
    arr.sort(reverse=True)
    arr_2 = list()
    for x in arr:
        if x != arr[0]:
            arr_2.append(x)
    return arr_2[0]
print(second_largest([1, 6, 3, 4, 5]))

