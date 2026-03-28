result = 1

b = float(input("Enter base: "))
n = int(input("Enter exponent: "))

if n > 0:
    for i in range(n):
        result = result * b
elif n < 0:
    for i in range(abs(n)):
        result = result * b
    result = 1 / result

print("Result:", result)