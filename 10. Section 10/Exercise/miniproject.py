
a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
 
def remove_elem(data, target):
    copy_data = data.copy()

    for item in data:
        if item == target:
            copy_data.remove(target)

    return copy_data
 
def get_product(data):
	total = 1
	for i in range(len(data)):
		total *= data.copy().pop()
	return total
 
print(remove_elem(c, 3))
print(a)
print(b)
print(get_product(b))
print(a)