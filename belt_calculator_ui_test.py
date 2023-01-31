import tkinter as tk

root = tk.Tk()
root.title("Dropdown Lists")

# Location of Idler dropdown list
Ki_Location_of_Idler_var = tk.StringVar()
Ki_Location_of_Idler_var.set("Choose Location of Idler")
Ki_Location_of_Idler_options = ["No Idler", "Belt slack side, inside of belt",
                                "Belt slack side, outside of belt", "Belt tight side, inside of belt", "Belt tight side, outside of belt"]
Ki_Location_of_Idler_dropdown = tk.OptionMenu(
    root, Ki_Location_of_Idler_var, *Ki_Location_of_Idler_options)
Ki_Location_of_Idler_dropdown.pack()

# Environment list
Ke_Environment_var = tk.StringVar()
Ke_Environment_var.set("Choose Environment")
Ke_Environment_options = ["Normal", "Frequent start and stop of machine",
                          "Hard to conduct maintenance checkup", "Dusty environment", "High temperature", "Oil or water splashing"]
Ke_Environment_dropdown = tk.OptionMenu(
    root, Ke_Environment_var, *Ke_Environment_options)
Ke_Environment_dropdown.pack()

# Dictionary to store values for each combination of options
values_Ki = {
    ("Belt slack side, inside of belt"): 0.0,
    ("Belt slack side, outside of belt"): 0.1,
    ("Belt tight side, inside of belt"): 0.1,
    ("Belt tight side, outside of belt"): 0.2,


    # Add other combinations and their values here
}

Ke_values = {

    ("Normal"): 0.0,
    ("Frequent start and stop of machine"): 0.2,
    ("Hard to conduct maintenance checkup"): 0.2,
    ("Dusty environment"): 0.2,
    ("High temperature"): 0.2,
    ("Oil or water splashing"): 0.2,

    # Add other combinations and their values here
}


def get_value_Ki():
    # Retrieve the selected options from each dropdown list
    Ki_Location_of_Idler = Ki_Location_of_Idler_var.get()

    # Retrieve the value for the selected combination of options
    values_Ki = values_Ki.get((Ki_Location_of_Idler), "Not Found")

    # Update the value label with the retrieved value
    value_Ki.config(text=f"Ki: {values_Ki}")


def get_Ke():

    # Retrieve the selected options from each dropdown list
    Ke_Environment = Ke_Environment_var.get()

    # Retrieve the value for the selected combination of options
    Ke = Ke_values.get((Ke_Environment), "Not Found")

    # Update the value label with the retrieved value
    Ke_label.config(text=f"Ke: {Ke}")


# Button to retrieve the value for the selected options
get_value_button = tk.Button(root, text="Get Value", command=get_value_Ki,)
get_value_button.pack()

# Label to display the value
value_Ki = tk.Label(root, text="")
value_Ki.pack()

Ke_label = tk.Label(root, text="")
Ke_label.pack()

root.mainloop()
