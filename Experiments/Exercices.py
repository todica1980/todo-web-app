filenames = ["1.Raw data.txt", "2.Reports.txt"]
n = 0
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    filenames[n] = filename
    n = n + 1
    print(filename)
print(filenames)


