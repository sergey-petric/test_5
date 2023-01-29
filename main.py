def compare_version(a, b):
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))
    print(a, b)
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


print(compare_version('2.10', '1.1.3'))
