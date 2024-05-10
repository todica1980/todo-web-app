todos = []

while True:
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.title())
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo.capitalize()
        case 'remove':
            number = int(input("Number of the todo to be removed: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")
