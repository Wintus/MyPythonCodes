def insert_sort(ls):
    size = len(ls)
    i = 1
    while i < size:
        tmp = ls[i]
        j = i - 1
        while j >= 0 and tmp < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = tmp
        i += 1
