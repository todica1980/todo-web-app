todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.title())
        case 'show' | 'display':  # Bitwise OR operator
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("wrong command was entered")

print("Bye!")