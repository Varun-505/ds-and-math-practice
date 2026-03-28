import math
a, b = map(int, input().split())
print("Coprime" if math.gcd(a, b) == 1 else "Not Coprime")