for i in range(6):
    for j in range(6 - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
for i in range(6-2,-1,-1):
    for j in range(6-i -1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
