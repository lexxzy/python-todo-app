import exerc1_func as Ex
import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet")
label2 = sg.Text("Enter Inches")
input_box1 = sg.Input()
input_box2 = sg.Input()
convert = sg.Button('Convert')
output_label = sg.Text("", key="output")
Window = sg.Window("Converter",
                  layout=[[label1,input_box1],
                          [label2,input_box2],
                          [convert,output_label ]])
while True:
    event, values = Window.read()
    print(event)
    print(values)

    feet = float(values[1])
    inche = float(values[0])
       
    new_convert=Ex.conv(feet , inche)
    Window['output'].update(value=f"{new_convert} m", text_color="green")
Window.close()

