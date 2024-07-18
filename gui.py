import functions
import FreeSimpleGUI as fsg
import time

fsg.theme("Black")

clock = fsg.Text('', key='clock')
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add", size=10)
list_box = fsg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            fsg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            fsg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Exit":
        break

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == fsg.WIN_CLOSED:
        break

window.close()
