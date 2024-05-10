while True:
    # Get user input and remove all space characters from it
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # Option 1
            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('files/todos.txt', 'r') as file:   # Option 2
                todos = file.readlines()

            todos.append(todo.capitalize())

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # Option 1:
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            # Option 2:
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')       # Option 3
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo.capitalize() + "\n"

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'remove':
            number = int(input("Number of the todo to be removed: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break

print("Bye!")

