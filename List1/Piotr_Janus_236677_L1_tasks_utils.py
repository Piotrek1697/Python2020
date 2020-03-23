def to_float(list):
    return [float(number) for number in list]


def to_int(list):
    return [int(number) for number in list]


def is_any_negative(list):
    return any(number < 0 for number in list)


def file_exists(file_name):
    exists = True
    try:
        f = open(file_name, "r")
        f.close()
    except:
        exists = False
    return exists
