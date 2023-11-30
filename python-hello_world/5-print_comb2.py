#program that prints numbers from 0 to 99
for i in range(100):
    print(f"{i:02d}", end=", " if i < 99 else "\n")