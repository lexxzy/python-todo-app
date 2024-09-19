import function
import FreeSimpleGUI as sg

text1 = sg.text("Enter Feet")
text2 = sg.text("Enter inches")
enter_feet = sg.InputText()
enter_inches = sg.InputText()
convert = sg.Button("Convert")

window = sg.window("Converter", 
                   Layout=[[text1,enter_feet],
                           [text2,enter_inches],
                           [convert]])
window.read()
window.close()
