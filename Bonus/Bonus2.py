contents = ["All carrots needs to be sliced "
            "longitudinally.",          # split a list and an item from a list
            "the carrots were reportedly sliced.",
            "the slicing process"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)

a = "I am a string" \
    " on my own"            # split a string
