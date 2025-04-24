from functions import get_todos, write_todos
import time 

now = time.strftime("%Y %b %d")
print("Today is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)
    elif user_action.startswith("show") in user_action:
        todos = get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index}.{item}")
    elif user_action.startswith("edit") in user_action:
        try:
            todos = get_todos()
            number = int(user_action[5:])
            new_todo = input("Enter new todo ")
            todos[int(number) - 1] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
          print("Your command is not valid.") 
          continue 
    elif user_action.startswith("complete") in user_action:
        try:
            todo = user_action[9:]
            todos = get_todos()
            todos.remove(todos[int(todo) - 1])
            write_todos(todos)
        except IndexError:
            print("There is no number ith that number.")
            continue
    elif user_action.startswith("exit") in user_action:
        break
    else:
        print("Command is not valid")

print("Bye!")