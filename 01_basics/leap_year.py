year = int(input("Enter the year: "))

if year % 4 == 0:
    print(f"The {year} is a Leap Year")
elif year % 400 == 0:
    print(f"The {year} is a Leap Year")
elif year % 100 == 0:
    print(f"The {year} is not a Leap Year")
else:
    print(f"The {year} is not a Leap Year")