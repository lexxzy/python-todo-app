import exerc1_func as Ex
import FreeSimpleGUI as sg
sg.theme("Black")
label1 = sg.Text("Enter feet")
label2 = sg.Text("Enter Inches")
input_box1 = sg.Input()
input_box2 = sg.Input()
Exit_1 = sg.Button("Exit")
convert = sg.Button('Convert')
output_label = sg.Text("", key="output")
Window = sg.Window("Converter",
                  layout=[[label1,input_box1],
                          [label2,input_box2],
                          [convert,output_label ],[Exit_1]])
while True:
    event, values = Window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            try:
                feet = float(values[1])
                inche = float(values[0])
            
                new_convert=Ex.conv(feet , inche)
                Window['output'].update(value=f"{new_convert} m", text_color="green")
            except ValueError:
                sg.popup("Please provide two numbers.")
        case "Exit":
            break
Window.close()

