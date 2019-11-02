import random

def formatter(d):
    x_d = random.uniform(0.75, 0.86)
    x_rest = 1 - x_d
    arr_val = [x_rest for x in range(9)]
    for x in range(9):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        k = random.uniform(0.02, 0.12)
        if(arr_val[j] - k > 0):
            arr_val[i] = arr_val[i] + k
            arr_val[j] = arr_val[j] - k
    dict_ = {}
    dict_[d] = x_d
    done = d
    i = 0
    for x in range(10):
        if x != d:
            dict_[x] = arr_val[i]
            i += 1
    list_ = sorted(dict_)
    new_dict = {}
    for key in list_:
        new_dict[key] = dict_[key]
    return new_dict