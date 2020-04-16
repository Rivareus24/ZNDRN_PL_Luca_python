# Exercise EX1: sub-list
def my_fun_1(items):
    return [item
            for item in items
            if len(item) > 5]


# Exercise EX2: maximum difference
def my_func_2(in_, out_):
    differences = [i_ - o_
                   for i_, o_ in zip(in_, out_)]
    return max(differences)


# Exercise EX3: filter largest
def my_func_3(dict_):
    # tolgo i false
    dict_true = {k: v
                 for k, v in dict_.items()
                 if v}

    largest_key = ''  # assuming there is at least on True value
    for k, v in dict_true.items():
        if len(k) > len(largest_key):
            largest_key = k
    return largest_key


# Exercise EX4: list union
def my_func_4(l1, l2):
    return list(set(l1 + l2))


# Exercise EX5: tri-sum
def my_func_5(numbers):
    return any(x + y + z == 0
               for i, x in enumerate(numbers)
               for j, y in enumerate(numbers)
               for k, z in enumerate(numbers)
               if i != j != k)


# Exercise EX6: string period
def my_func_6(string_):
    for i in range(1, int(len(string_) / 2)):
        if len(string_) % i != 0:
            continue
        pattern = string_[:i]
        if pattern * int(len(string_) / i) == string_:
            return i
    return 0
