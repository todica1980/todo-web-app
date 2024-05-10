DEFAULT_FILEPATH = "files/todos.txt"


def get_todos(filepath=DEFAULT_FILEPATH):    # default argument
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=DEFAULT_FILEPATH):    # default argument should be at the end
    """ Write the to-do items list in the next file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)