filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(filename, "r")
    content = file.read()
    file.close()
    print(content)