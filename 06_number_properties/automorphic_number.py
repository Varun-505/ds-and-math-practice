n = int(input())
sq = n * n
print("Automorphic" if str(sq).endswith(str(n)) else "Not Automorphic")