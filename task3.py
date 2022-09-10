n = int(input())
for i in range(1, n+1):
    y = 1
    for j in range(i):
        print(y, end=' ')
        y += 1
    print()
