def compare_version(a, b):
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


print(compare_version('1.10', '1.1'))
