import math
n = input()
print("Strong" if int(n) == sum(math.factorial(int(d)) for d in n) else "Not Strong")