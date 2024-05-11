#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = []
    list_b = []
    list_a.extend(tuple_a)
    list_b.extend(tuple_b)
    if len(list_a) >= 2 and len(list_b) >= 2:
        c = list_a[0] + list_b[0]
        d = list_a[1] + list_b[1]
        new_tuple = (c, d)
        return new_tuple
    elif len(list_b) < 2:
        if len(list_b) == 1:
            list_b.append(0)
        elif len(list_b) == 0:
            list_b.append(0)
            list_b.append(0)
        c = list_a[0] + list_b[0]
        d = list_a[1] + list_b[1]
        new_tuple = (c, d)
        return new_tuple
    elif len(list_a) < 2:
        if len(list_a) == 1:
            list_a.append(0)
        elif len(list_a) == 0:
            list_a.append(0)
            list_a.append(0)
        c = list_a[0] + list_b[0]
        d = list_a[1] + list_b[1]
        new_tuple = (c, d)
        return new_tuple
