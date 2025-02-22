def revtriangle(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)

revtriangle(5)

print("----------------------------------------")


def diamond(n):
    for i in range(1, n + 1, 2):
        print('  ' * ((n - i) // 2) + '* ' * i)

    for i in range(n - 2, 0, -2):
        print('  ' * ((n - i) // 2) + '* ' * i)


diamond(7)