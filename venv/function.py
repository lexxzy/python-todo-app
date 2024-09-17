def get_todo():
    """Read a Text file and retrun the list of to-do items"""
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
    return todos
    
def write_todo(wri):
    """Write a to-do as a list to a text file"""
    with open('todo.txt', 'w') as file:
        file.writelines(wri)