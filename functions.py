FILEPATH = "todos.txt" #constat (uppercase)

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list
    of to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines() #creates a list with the items in the text file
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH): #NON-Default parameters go before default parameters
    with open(filepath, "w") as file_local:  # creating a new file that overwrites the existing file
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())