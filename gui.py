import os
import functions
import FreeSimpleGUI as sg
import time

if not os.path.exist("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

clock = sg.Text('', key="clock")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), 
                      key='todos', 
                      enable_events=True, 
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window('My To-Do App', 
                    layout=[
                    [clock],
                    [label], 
                    [input_box, add_button],
                    [list_box, edit_button, complete_button],
                    [exit_button]], 
                    font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b, %d, %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!")
        case "Complete":
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()

                todos.remove(todos.index(todo))
                functions.write_todos()
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
