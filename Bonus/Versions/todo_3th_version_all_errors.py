while True:
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('../../files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.capitalize() + "\n")

        with open('../../files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('../../files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('../../files/todos.txt', 'r') as file:
                todos = file.readlines()
            if number <= len(todos):

                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo.capitalize() + "\n"

                with open('../../files/todos.txt', 'w') as file:
                    file.writelines(todos)
            else:
                print("Enter a valid todo number")
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("remove"):
        try:
            number = int(user_action[6:])

            with open('../../files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('../../files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with this number")
            continue
        except ValueError:
            print("Enter a valid number!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")
