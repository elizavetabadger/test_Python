def opi(string):
    some_list = list(string.split())
    a, b, op = float(some_list[0]), float(some_list[2]), some_list[1]
    return a, b, op
