# for loop
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

total = 0

for num in range(a, b + 1):
    total += num

print("Sum:", total)

'''
start = int(input("Enter a number: "))
stop = int(input("Enter a number: "))
total = sum(range(start, stop + 1))
print(total) 
'''