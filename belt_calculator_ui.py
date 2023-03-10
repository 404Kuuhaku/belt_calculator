import math
import tkinter as tk
from tkinter import ttk


# Create the main window
root = tk.Tk()
root.title("Belt Selector")

# Driven Machine dropdown list
driven_machine_var = tk.StringVar()
driven_machine_var.set("Choose Driven Machine")
driven_machine_options = ["Type 1", "Type 2", "Type 3", "Type 4"]
driven_machine_dropdown = tk.OptionMenu(root, driven_machine_var, *driven_machine_options)
driven_machine_dropdown.pack()

# Driving Unit / Motor dropdown list
driving_unit_var = tk.StringVar()
driving_unit_var.set("Choose Driving Unit/Motor")
driving_unit_options = ["Max power < 300 % of rated power", "Max power > 300 % of rated power"]
driving_unit_dropdown = tk.OptionMenu(root, driving_unit_var, *driving_unit_options)
driving_unit_dropdown.pack()

# Running time (hrs./day) dropdown list
running_time_var = tk.StringVar()
running_time_var.set("Choose Running Time (hrs./day)")
running_time_options = ["3-5 hours", "8-12 hours", "16-24 hours"]
running_time_dropdown = tk.OptionMenu(root, running_time_var, *running_time_options)
running_time_dropdown.pack()

# Dictionary to store values for each combination of options
values_Ko = {("Type 1", "Max power < 300 % of rated power", "3-5 hours"): 1.0,
          ("Type 1", "Max power < 300 % of rated power", "8-12 hours"): 1.1,
          ("Type 1", "Max power < 300 % of rated power", "16-24 hours"): 1.2,

          ("Type 2", "Max power < 300 % of rated power", "3-5 hours"): 1.1,
          ("Type 2", "Max power < 300 % of rated power", "8-12 hours"): 1.2,
          ("Type 2", "Max power < 300 % of rated power", "16-24 hours"): 1.3,

          ("Type 3", "Max power < 300 % of rated power", "3-5 hours"): 1.2,
          ("Type 3", "Max power < 300 % of rated power", "8-12 hours"): 1.3,
          ("Type 3", "Max power < 300 % of rated power", "16-24 hours"): 1.4,

          ("Type 4", "Max power < 300 % of rated power", "3-5 hours"): 1.3,
          ("Type 4", "Max power < 300 % of rated power", "8-12 hours"): 1.4,
          ("Type 4", "Max power < 300 % of rated power", "16-24 hours"): 1.5,



          ("Type 1", "Max power > 300 % of rated power", "3-5 hours"): 1.1,
          ("Type 1", "Max power > 300 % of rated power", "8-12 hours"): 1.2,
          ("Type 1", "Max power > 300 % of rated power", "16-24 hours"): 1.3,

          ("Type 2", "Max power > 300 % of rated power", "3-5 hours"): 1.2,
          ("Type 2", "Max power > 300 % of rated power", "8-12 hours"): 1.3,
          ("Type 2", "Max power > 300 % of rated power", "16-24 hours"): 1.4,

          ("Type 3", "Max power > 300 % of rated power", "3-5 hours"): 1.4,
          ("Type 3", "Max power > 300 % of rated power", "8-12 hours"): 1.5,
          ("Type 3", "Max power > 300 % of rated power", "16-24 hours"): 1.6,

          ("Type 4", "Max power > 300 % of rated power", "3-5 hours"): 1.5,
          ("Type 4", "Max power > 300 % of rated power", "8-12 hours"): 1.6,
          ("Type 4", "Max power > 300 % of rated power", "16-24 hours"): 1.8,
          # Add other combinations and their values here
         }



def calculate():
    # Retrieve the selected options from each dropdown list
    driven_machine = driven_machine_var.get()
    driving_unit = driving_unit_var.get()
    running_time = running_time_var.get()

    # Retrieve the value for the selected combination of options
    value_Ko = values_Ko.get((driven_machine, driving_unit, running_time), "Not Found")
    
    # Update the value label with the retrieved value
    value_Ko_label.config(text=f"Ko : {value_Ko}")


    D = float(D_entry.get())
    d = float(d_entry.get())
    C = float(C_entry.get())

    # Perform calculations here using the input values
    if (D+d)/2 < C:
        result_label.config(text="Distance between centers of pulley is ok")
    else:
        result_label.config(text="Distance between centers of pulley is too short", fg="red")

    SR = D / d
    L = 2 * C + (math.pi / 2) * (D + d) + (D - d)**2 / (4 * C)
    
    
    # Display the results
    SR_label.config(text="SR: " + str(SR))
    L_label.config(text="L: " + str(L))
    


    Pt = float(Pt_entry.get())
    Speed = float(Speed_entry.get())
    Environment = int(Environment_entry.get())


# Create the input frame
input_frame = ttk.Frame(root)
input_frame.pack()

# Create the input labels and entries
D_label = ttk.Label(input_frame, text="Enter a value for D(inch):")
D_label.grid(row=0, column=0)
D_entry = ttk.Entry(input_frame)
D_entry.grid(row=0, column=1)

d_label = ttk.Label(input_frame, text="Enter a value for d(inch):")
d_label.grid(row=1, column=0)
d_entry = ttk.Entry(input_frame)
d_entry.grid(row=1, column=1)

C_label = ttk.Label(input_frame, text="Enter a value for C(inch):")
C_label.grid(row=2, column=0)
C_entry = ttk.Entry(input_frame)
C_entry.grid(row=2, column=1)

Pt_label = ttk.Label(input_frame, text="Enter a value for Pt(Hp):")
Pt_label.grid(row=3, column=0)
Pt_entry = ttk.Entry(input_frame)
Pt_entry.grid(row=3, column=1)

Speed_label = ttk.Label(input_frame, text="Enter a value for Speed(rpm):")
Speed_label.grid(row=4, column=0)
Speed_entry = ttk.Entry(input_frame)
Speed_entry.grid(row=4, column=1)

Environment_label = ttk.Label(input_frame, text="Enter a value for Environment:")
Environment_label.grid(row=6, column=0)
Environment_entry = ttk.Entry(input_frame)
Environment_entry.grid(row=6, column=1)





# Create a button to initiate the calculation
calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate)
calculate_button.grid(row=7, column=0, columnspan=2, pady=10)


# Create a label to display the result

value_Ko_label = tk.Label(root, text="")
value_Ko_label.pack()

result_label = tk.Label(input_frame)
result_label.grid(row=8, column=0, columnspan=2)


SR_label = ttk.Label(input_frame)
SR_label.grid(row=9, column=0, columnspan=2)


L_label = ttk.Label(input_frame)
L_label.grid(row=10, column=0, columnspan=2)


root.mainloop()