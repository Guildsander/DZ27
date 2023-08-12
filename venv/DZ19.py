def common_elements():
    lst_3 = [x for x in range(1, 101) if x % 3 == 0]
    lst_5 = [x for x in range(1, 101) if x % 5 == 0]

    set_3 = set(lst_3)
    set_5 = set(lst_5)
    common_set = set_3.intersection(set_5)
    return common_set
rezult = common_elements()
print(rezult)


