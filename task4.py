n = int(input())

for i in range(n, 0, -1):
    for _ in range(0, i):
        print(i, end=' ')
    print()
