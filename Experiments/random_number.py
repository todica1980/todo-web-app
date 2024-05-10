import random

number_1 = input("Enter the lower bound: ")
number_2 = input("Enter the upper bound: ")

random_number = random.randint(int(number_1), int(number_2))
print (random_number)