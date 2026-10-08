def max_number(a):
    s = 0
    for i in a:
        if i > s:
            s = i
    return s


def tak_jup(num):
    if num % 2 == 0:
        print('Жуп сан')
    else:
        print('Так Сан')

