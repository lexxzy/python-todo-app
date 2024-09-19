#todos = []
from function import get_todo,write_todo
while True: 
    user_prompt = input("Type add , show, complete, edit or exit: ")
    user_prompt = user_prompt.strip()
     # If the response from the user is equal "add"
    if user_prompt.startswith("add") and user_prompt[4:] != '':

        todo = user_prompt[3:] + "\n"
        # this is to make sure python is reading the existing to-do from the file before adding new todo to the list
        todos = get_todo()
        
        #file = open('todo.txt', 'r')
        #todos = file.readlines()
        #file.close()
        # Writing the new todo into the file
        todos.append(todo)

        write_todo(todos)

        #file = open('todo.txt', 'w')
        #file.writelines(todos)
        #file.close()

    elif user_prompt.startswith("show") :
        print("Showing your todo list :")
        todos = get_todo()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1 }.{item}"
            print(row)
            
    elif user_prompt.startswith("complete"):
        try: 
            todos = get_todo() 
            number = int(user_prompt[8:])
            number = number - 1 
            rem_todo = todos.pop(number)
            todos=write_todo(todos)
            for item in todos or []:
                print(enumerate(item))
        except ValueError:
            print("Pick A number to remove: ")
            continue
        except IndexError:
            print("The number picked is out of range: ")
            continue

    elif user_prompt.startswith("edit"):
        try:
            todos = get_todo()
            number = int(user_prompt[5:])
            print(number)
            number = number - 1
            new_todo = input("What is your new todo: ") + '\n'
            todos[number] = new_todo
            todo = write_todo(todos)
            for item in todos or []:
                print(item)
        except ValueError:
            print("Pick A number to remove: ")
            continue
        except IndexError:
            print("The number picked is out of range: ")
            continue

    elif user_prompt.startswith("exit"):
        break
    else:
        print("Please Enter a Valid command")
print('Bye!')