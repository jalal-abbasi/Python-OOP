a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c


def remove_elem(data, target):
    data2 = data[:]
    for item in data2:
        if item == target:
            data2.remove(target)
    return data2


def get_product(data):
    total = 1
    data2 = data[:]
    for i in range(len(data2)):
        total *= data2.pop()
    return total


remove_elem(c, 3)
print(get_product(b))
print(a)