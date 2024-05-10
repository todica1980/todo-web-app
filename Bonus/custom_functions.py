from Bonus.bonus_functions import parse
from Bonus.convert_function import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("kid is too small.")
else:
    print("kid can use the slide.")