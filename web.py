import streamlit as st
from streamlit import session_state
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field after adding

todos = functions.get_todos()

# Use Streamlit's built-in styling options
st.set_page_config(page_title="Minimalistic Todo-app", layout="centered")

st.title("Minimalistic Todo-app")
st.markdown("*Increase your productivity.*")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo + str(index))
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo + str(index)]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

