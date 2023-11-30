#This program that prints all possible different combinations of two digits.
for i in range(10):
    for x in range(i + 1, 10):
        if i < 8:
            print('{:02}'.format(i * 10 + x), end=", ")
        else:
            print('{:02}'.format(i * 10 + x))