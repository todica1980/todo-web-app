import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("This is my todo application")
st.write("This app is to improve my Python skills")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

print("Hello")
st.session_state