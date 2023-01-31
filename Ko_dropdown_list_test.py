import tkinter as tk

root = tk.Tk()
root.title("Dropdown Lists")

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

def get_value_Ko():
    # Retrieve the selected options from each dropdown list
    driven_machine = driven_machine_var.get()
    driving_unit = driving_unit_var.get()
    running_time = running_time_var.get()

    # Retrieve the value for the selected combination of options
    value_Ko = values_Ko.get((driven_machine, driving_unit, running_time), "Not Found")
    
    # Update the value label with the retrieved value
    value_Ko_label.config(text=f"Ko : {value_Ko}")

# Button to retrieve the value for the selected options
get_value_button = tk.Button(root, text="Get Value", command=get_value_Ko)
get_value_button.pack()

# Label to display the value
value_Ko_label = tk.Label(root, text="")
value_Ko_label.pack()

root.mainloop()
