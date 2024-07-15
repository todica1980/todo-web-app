import streamlit as st
import functions

todos = functions.get_todos()
st.title("My todo app")
st.subheader("This is my todo application")
st.write("This app is to improve my Python skills")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add new todo...")

print("Hello")