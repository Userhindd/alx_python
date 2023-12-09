import sys

args = sys.argv[1:]

if len(args) == 0:
    print("0 arguments.")
else:
    print(f"{len(args)} {'argument' if len(args) == 1 else 'arguments'}:")
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")