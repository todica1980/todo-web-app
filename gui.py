import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('My to do app', layout=[[label], [input_box, add_button]])
window.read()
window.close()