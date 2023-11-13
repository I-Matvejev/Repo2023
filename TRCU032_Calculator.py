import tkinter as tk

root = tk.Tk()
root.title('TR CU 032/2013 Calculator')
root.geometry('400x340')
root.resizable(False, False)


def open_convert_window():
    convertWindow = tk.Toplevel()
    convertWindow.title('X to MPa')
    convertWindow.geometry('250x80')
    convertWindow.resizable(False, False)

    options = ['kPa', 'bar', 'atm', 'psi', 'kgf/cm2']
    variable = tk.StringVar(convertWindow)
    variable.set('kPa')
    droplist = tk.OptionMenu(convertWindow, variable, *options)
    droplist.place(x=20, y=25)

    pressure_entry = tk.Entry(convertWindow, width=10)
    pressure_entry.place(x=120, y=30)

    def set_button_command():
        value = float(pressure_entry.get())
        unit = variable.get()

        pressureMPa = None
        if unit == 'kPa':
            pressureMPa = value / 1000
        elif unit == 'bar':
            pressureMPa = value / 10
        elif unit == 'atm':
            pressureMPa = value / 9.869
        elif unit == 'psi':
            pressureMPa = value / 145
        elif unit == 'kgf/cm2':
            pressureMPa = value / 10.197

        result = f'{pressureMPa: .3f}'

        pressure_entry_main.delete(0, "end")
        pressure_entry_main.insert(0, result)

        convertWindow.destroy()

    set_button = tk.Button(convertWindow, bd=5, text='Set', command=set_button_command)
    set_button.place(x=200, y=25)


def open_info_window():
    infoWindow = tk.Toplevel()
    infoWindow.title('Group 1&2')
    infoWindow.geometry('350x100')
    infoWindow.resizable(False, False)

    info_label = tk.Label(infoWindow, text='"Group 1: Media consisting of \n flammable, oxidizable, combustible, '
                                           'explosive, \n toxic and highly toxic gases, liquids and vapours \n in a '
                                           'single phase and their mixtures. \n Group 2: All other media except those '
                                           'belonging to Group 1."')
    info_label.pack()


def result_window(result):
    result_text.configure(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result, "center")


def valve_pipeline_function_1(volume_DN_value, pressure_PN_value):
    if gas_liquid_radio_button_var.get() == 0:
        valve_pipeline_function_2(volume_DN_value, pressure_PN_value)
    else:
        valve_pipeline_function_3(volume_DN_value, pressure_PN_value)


def valve_pipeline_function_2(volume_DN_value, pressure_PN_value):
    if group1_group2_radio_button_var.get() == 0:
        valve_pipeline_function_4(volume_DN_value, pressure_PN_value)
    else:
        valve_pipeline_function_5(volume_DN_value, pressure_PN_value)


def valve_pipeline_function_4(volume_DN_value, pressure_PN_value):  # Gas Group1
    if 25 < volume_DN_value <= 100 and 0.05 < pressure_PN_value and volume_DN_value * pressure_PN_value <= 100:
        result = 'Category 1\nDeclaration of Conformity'
    elif 25 < volume_DN_value <= 100 and 1 < pressure_PN_value and 100 < volume_DN_value * pressure_PN_value or 100 < volume_DN_value <= 350 and 0.05 < pressure_PN_value and volume_DN_value * pressure_PN_value <= 350:
        result = 'Category 2\nDeclaration of Conformity'
    elif 100 < volume_DN_value <= 350 and 1 < pressure_PN_value and 350 < volume_DN_value * pressure_PN_value or 350 < volume_DN_value and 0.05 < pressure_PN_value:
        result = 'Category 3\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def valve_pipeline_function_5(volume_DN_value, pressure_PN_value):  # Gas Group2
    if 32 < volume_DN_value <= 100 and 0.05 < pressure_PN_value and 100 < volume_DN_value * pressure_PN_value or 100 < volume_DN_value and 0.05 < pressure_PN_value and 100 < volume_DN_value * pressure_PN_value <= 350:
        result = 'Category 1\nDeclaration of Conformity'
    elif 100 < volume_DN_value <= 250 and 0.05 < pressure_PN_value and 350 < volume_DN_value * pressure_PN_value or 250 < volume_DN_value and 0.05 < pressure_PN_value and 350 < volume_DN_value * pressure_PN_value <= 500:
        result = 'Category 2\nDeclaration of Conformity'
    elif 250 < volume_DN_value and 0.05 < pressure_PN_value and 500 < volume_DN_value * pressure_PN_value:
        result = 'Category 3\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def valve_pipeline_function_3(volume_DN_value, pressure_PN_value):
    if group1_group2_radio_button_var.get() == 0:
        valve_pipeline_function_6(volume_DN_value, pressure_PN_value)
    else:
        valve_pipeline_function_7(volume_DN_value, pressure_PN_value)


def valve_pipeline_function_6(volume_DN_value, pressure_PN_value):  # Liquid Group1
    if 25 < volume_DN_value and 0.05 < pressure_PN_value <= 1 and 200 < volume_DN_value * pressure_PN_value:
        result = 'Category 1\nDeclaration of Conformity'
    elif 25 < volume_DN_value and 1 < pressure_PN_value <= 50 and 200 < volume_DN_value * pressure_PN_value:
        result = 'Category 2\nDeclaration of Conformity'
    elif 25 < volume_DN_value and 50 < pressure_PN_value:
        result = 'Category 3\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def valve_pipeline_function_7(volume_DN_value, pressure_PN_value):  # Liquid Group2
    if 200 < volume_DN_value and 1 < pressure_PN_value <= 50 and 500 < volume_DN_value * pressure_PN_value:
        result = 'Category 1\nDeclaration of Conformity'
    elif 200 < volume_DN_value and 50 < pressure_PN_value:
        result = 'Category 2\nDeclaration of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def pressure_vessel_function_1(volume_DN_value, pressure_PN_value):
    if gas_liquid_radio_button_var.get() == 0:
        pressure_vessel_function_2(volume_DN_value, pressure_PN_value)
    else:
        pressure_vessel_function_3(volume_DN_value, pressure_PN_value)


def pressure_vessel_function_2(volume_DN_value, pressure_PN_value):
    if group1_group2_radio_button_var.get() == 0:
        pressure_vessel_function_4(volume_DN_value, pressure_PN_value)
    else:
        pressure_vessel_function_5(volume_DN_value, pressure_PN_value)


def pressure_vessel_function_4(volume_DN_value, pressure_PN_value):  # Gas Group1
    if 0.001 < volume_DN_value and 0.05 < pressure_PN_value and 0.0025 < volume_DN_value * pressure_PN_value <= 0.005:
        result = 'Category 1\nDeclaration of Conformity'
    elif 0.001 < volume_DN_value and 0.05 < pressure_PN_value and 0.005 < volume_DN_value * pressure_PN_value <= 0.02:
        result = 'Category 2\nDeclaration of Conformity'
    elif 0.0001 < volume_DN_value <= 0.001 and 20 < pressure_PN_value <= 100 or 0.001 < volume_DN_value and 0.05 < pressure_PN_value and 0.02 < volume_DN_value * pressure_PN_value <= 0.1:
        result = 'Category 3\nCertificate of Conformity'
    elif 0.0001 < volume_DN_value <= 0.001 and 100 < pressure_PN_value or 0.001 < volume_DN_value and 0.05 < pressure_PN_value and 0.1 < volume_DN_value * pressure_PN_value:
        result = 'Category 4\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def pressure_vessel_function_5(volume_DN_value, pressure_PN_value):  # Gas Group2
    if 0.001 < volume_DN_value <= 0.4 and 0.05 < pressure_PN_value <= 20 and 0.005 < volume_DN_value * pressure_PN_value <= 0.02:
        result = 'Category 1\nDeclaration of Conformity'
    elif 0.001 < volume_DN_value <= 2 and 0.05 < pressure_PN_value <= 100 and 0.02 < volume_DN_value * pressure_PN_value <= 0.1:
        result = 'Category 2\nDeclaration of Conformity'
    elif 0.0001 < volume_DN_value <= 0.001 and 100 < pressure_PN_value <= 300 or 0.001 < volume_DN_value <= 0.75 and 0.05 < pressure_PN_value and 0.1 < volume_DN_value * pressure_PN_value <= 0.3 or 0.75 < volume_DN_value and 0.05 < pressure_PN_value <= 0.4 and 0.1 < volume_DN_value * pressure_PN_value:
        result = 'Category 3\nCertificate of Conformity'
    elif 0.0001 < volume_DN_value <= 0.001 and 300 < pressure_PN_value or 0.001 < volume_DN_value and 0.4 < pressure_PN_value and 0.3 < volume_DN_value * pressure_PN_value:
        result = 'Category 4\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def pressure_vessel_function_3(volume_DN_value, pressure_PN_value):
    if group1_group2_radio_button_var.get() == 0:
        pressure_vessel_function_6(volume_DN_value, pressure_PN_value)
    else:
        pressure_vessel_function_7(volume_DN_value, pressure_PN_value)


def pressure_vessel_function_6(volume_DN_value, pressure_PN_value):  # Liquid Group1
    if 0.02 < volume_DN_value and 0.05 < pressure_PN_value <= 1 and 0.02 < volume_DN_value * pressure_PN_value:
        result = 'Category 1\nDeclaration of Conformity'
    elif 0.0001 < volume_DN_value <= 0.001 and 50 < pressure_PN_value or 0.001 < volume_DN_value and 1 < pressure_PN_value <= 50 and 0.02 < volume_DN_value * pressure_PN_value:
        result = 'Category 2\nDeclaration of Conformity'
    elif 0.001 < volume_DN_value and 50 < pressure_PN_value:
        result = 'Category 3\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def pressure_vessel_function_7(volume_DN_value, pressure_PN_value):  # Liquid Group2
    if 0.0001 < volume_DN_value <= 0.01 and 100 < pressure_PN_value or 0.02 < volume_DN_value and 1 < pressure_PN_value <= 50 and 1 < volume_DN_value * pressure_PN_value:
        result = 'Category 1\nDeclaration of Conformity'
    elif 0.01 < volume_DN_value and 50 < pressure_PN_value and 1 < volume_DN_value * pressure_PN_value:
        result = 'Category 2\nDeclaration of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def boiler_function_1(volume_DN_value, pressure_PN_value):
    if 0.002 < volume_DN_value and 0.05 < pressure_PN_value and volume_DN_value * pressure_PN_value <= 0.005:
        result = 'Category 1\nDeclaration of Conformity'
    elif 0.002 < volume_DN_value and 0.05 < pressure_PN_value <= 3.2 and 0.005 < volume_DN_value * pressure_PN_value <= 0.02:
        result = 'Category 2\nDeclaration of Conformity'
    elif 0.002 < volume_DN_value <= 1 and 0.05 < pressure_PN_value <= 3.2 and 0.02 < volume_DN_value * pressure_PN_value <= 0.3:
        result = 'Category 3\nCertificate of Conformity'
    elif 0.002 < volume_DN_value and 3.2 < pressure_PN_value or 0.002 < volume_DN_value <= 1 and 0.05 < pressure_PN_value <= 3.2 and 0.3 < volume_DN_value * pressure_PN_value or 1 < volume_DN_value and 0.05 < pressure_PN_value <= 3.2:
        result = 'Category 4\nCertificate of Conformity'
    else:
        result = 'NOT SUBJECT TO\nTR CU 032/2013'

    result_window(result)


def calculate_button_command():

    pressure_PN_value = float(pressure_entry_main.get())
    volume_DN_value = float(volume_entry.get())
    if valve_pipeline_pressure_vessel_boiler_radio_button_var.get() == 1:
        valve_pipeline_function_1(volume_DN_value, pressure_PN_value)
    elif valve_pipeline_pressure_vessel_boiler_radio_button_var.get() == 0:
        pressure_vessel_function_1(volume_DN_value, pressure_PN_value)
    elif valve_pipeline_pressure_vessel_boiler_radio_button_var.get() == 2:
        boiler_function_1(volume_DN_value, pressure_PN_value)


def boiler_radio_button_command():
    gas_radio_button.configure(state=tk.DISABLED)
    liquid_radio_button.configure(state=tk.DISABLED)
    group1_radio_button.configure(state=tk.DISABLED)
    group2_radio_button.configure(state=tk.DISABLED)

    pressure_label.configure(text='Design Pressure, MPa')
    volume_label.configure(text='Volume, m3')


def valve_pipeline_radio_button_command():
    gas_radio_button.configure(state=tk.NORMAL)
    liquid_radio_button.configure(state=tk.NORMAL)
    group1_radio_button.configure(state=tk.NORMAL)
    group2_radio_button.configure(state=tk.NORMAL)

    pressure_label.configure(text='PN, MPa')
    volume_label.configure(text='DN, mm')


def pressure_vessel_radio_button_command():
    gas_radio_button.configure(state=tk.NORMAL)
    liquid_radio_button.configure(state=tk.NORMAL)
    group1_radio_button.configure(state=tk.NORMAL)
    group2_radio_button.configure(state=tk.NORMAL)

    pressure_label.configure(text='Design Pressure, MPa')
    volume_label.configure(text='Volume, m3')


valve_pipeline_pressure_vessel_boiler_radio_button_var = tk.IntVar()
valve_pipeline_pressure_vessel_boiler_radio_button_var.set(0)

valve_pipeline_radio_button = tk.Radiobutton(root, text='Valve/Pipeline', variable=valve_pipeline_pressure_vessel_boiler_radio_button_var, value=1, command=valve_pipeline_radio_button_command)
valve_pipeline_radio_button.place(x=15, y=15)

pressure_vessel_radio_button = tk.Radiobutton(root, text='Pressure vessel', variable=valve_pipeline_pressure_vessel_boiler_radio_button_var, value=0, command=pressure_vessel_radio_button_command)
pressure_vessel_radio_button.place(x=155, y=15)

boiler_radio_button = tk.Radiobutton(root, text='Boiler', variable=valve_pipeline_pressure_vessel_boiler_radio_button_var, value=2, command=boiler_radio_button_command)
boiler_radio_button.place(x=295, y=15)

convert_button = tk.Button(root, bd=5, bg='#D2D3D3', text='Convert', width=8, command=open_convert_window)
convert_button.place(x=130, y=85)

gas_liquid_radio_button_var = tk.BooleanVar()
gas_liquid_radio_button_var.set(0)

gas_radio_button = tk.Radiobutton(root, text='Gas', variable=gas_liquid_radio_button_var, value=0)
gas_radio_button.place(x=10, y=145)

liquid_radio_button = tk.Radiobutton(root, text='Liquid', variable=gas_liquid_radio_button_var, value=1)
liquid_radio_button.place(x=90, y=145)

group1_group2_radio_button_var = tk.BooleanVar()
group1_group2_radio_button_var.set(0)

group1_radio_button = tk.Radiobutton(root, text='Group 1', variable=group1_group2_radio_button_var, value=0)
group1_radio_button.place(x=195, y=145)

group2_radio_button = tk.Radiobutton(root, text='Group 2', variable=group1_group2_radio_button_var, value=1)
group2_radio_button.place(x=315, y=145)

info_button = tk.Button(root, bd=5, bg='#D2D3D3', text='i', width=3, command=open_info_window)
info_button.place(x=272, y=143)

calculate_button = tk.Button(root, bd=5, bg='#D2D3D3', text='CALCULATE', command=calculate_button_command)
calculate_button.place(x=160, y=190)

pressure_label = tk.Label(root, text='Design Pressure, MPa')
pressure_label.place(x=50, y=62)

volume_label = tk.Label(root, text='Volume, m3')
volume_label.place(x=280, y=62)

pressure_entry_main = tk.Entry(root, width=10)
pressure_entry_main.place(x=50, y=90)

volume_entry = tk.Entry(root, width=10)
volume_entry.place(x=280, y=90)

separator_label = tk.Label(root, text='------------------------------RESULT------------------------------')
separator_label.place(x=25, y=235)

result_text = tk.Text(root)
result_text.tag_configure("center", justify=tk.CENTER)
result_text.place(x=70, y=270, height=40, width=250)

created_by_label = tk.Label(root, text='by Ilya Matvejev')
created_by_label.place(x=2, y=320)
created_by_label.configure(font=("Courier", 8, "italic"))

version_label = tk.Label(root, text='version 2.2')
version_label.place(x=313, y=320)
version_label.configure(font=("Courier", 8, "italic"))


root.mainloop()
