import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My ToDo App")
st.subheader("This is my todo app.")

for index, todo in enumerate(todos):
    clean_todo = todo.strip()
    checkbox = st.checkbox(clean_todo, key=clean_todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[clean_todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo: ", 
              on_change=add_todo, key='new_todo')
