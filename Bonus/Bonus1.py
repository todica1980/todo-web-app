text = input("Enter a title: ")

length = len(text)

print("The length of the title is:", length)

password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password was correct!")


x = 1

while x <= 6:
    print(x)
    x = x + 1