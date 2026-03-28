# while loop
'''
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of first {n} natural numbers is: {total}")
'''   

# for loop
''' 
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of first {n} natural numbers is: {total}")   
'''

# recursion

def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n - 1)

n = int(input("Enter a number: "))
print(f"Sum of first {n} natural numbers is: {sum_recursive(n)}")   
