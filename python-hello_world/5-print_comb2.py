#program that prints numbers from 0 to 99
for i in range(100):
    last = ', ' if i < 99 else '\n'
    print('{:02}{}'.format(i, last), end="")