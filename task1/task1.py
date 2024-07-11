arg = [int(n) for n in input().split()]
arr = arg[0] * [i for i in range(1, arg[0] + 1)]
i = 1
while True:
    print(i, end='')
    i = 1 + (i + arg[1] - 2) % arg[0]
    if i == 1:
        break
