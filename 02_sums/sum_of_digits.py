# while loop
num = 432109876

sum_digits = 0

while num > 0:
    digit = num % 10       # Extract last digit
    sum_digits += digit    # Add to sum
    num = num // 10        # Remove last digit

print("Sum of digits:", sum_digits)