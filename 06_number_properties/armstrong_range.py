a, b = map(int, input().split())

for n in range(a, b+1):
    s = str(n)
    p = len(s)
    if n == sum(int(d)**p for d in s):
        print(n, end=" ")