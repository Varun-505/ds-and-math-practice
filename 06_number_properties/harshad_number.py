n = int(input())
s = sum(int(d) for d in str(n))
print("Harshad" if n % s == 0 else "Not Harshad")