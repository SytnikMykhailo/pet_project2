def get_todos(filepath = 'todos.txt'):
    """ Read a text file and return the list of 
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath = 'todos.txt'):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos)
    