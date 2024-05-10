
member = input("Enter a new member: ")

file = open("members.txt", "r")
member_list = file.readlines()
file.close()

member_list.append(member + "\n")

file = open("members.txt", "w")
file.writelines(member_list)
file.close()

