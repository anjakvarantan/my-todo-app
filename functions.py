FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH): #function definition
    """ Read a text file and return the list of
    to-do items. OVO JE DOC STRING
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# print(help(get_todos))

def write_todos(todos_arg,filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file2:
        file2.writelines(todos_arg)

print("Hello from functions")
