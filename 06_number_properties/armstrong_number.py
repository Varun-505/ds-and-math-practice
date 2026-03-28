n = input()
power = len(n)
print("Armstrong" if int(n) == sum(int(d)**power for d in n) else "Not Armstrong")