import tkinter as tk

root = tk.Tk()
root.title("Dropdown Lists")

# Environment list
Environment_var = tk.StringVar()
Environment_var.set("Choose Environment")
Environment_options = ["Normal", "Frequent start and stop of machine","Hard to conduct maintenance checkup", "Dusty environment", "High temperature", "Oil or water splashing"]
Environment_dropdown = tk.OptionMenu(root, Environment_var, *Environment_options)
Environment_dropdown.pack()

values_Ke = {

    ("Normal"): 0.0,
    ("Frequent start and stop of machine"): 0.2,
    ("Hard to conduct maintenance checkup"): 0.2,
    ("Dusty environment"): 0.2,
    ("High temperature"): 0.2,
    ("Oil or water splashing"): 0.2,

    # Add other combinations and their values here
}


def get_value_Ke():

    # Retrieve the selected options from each dropdown list
    Environment = Environment_var.get()

    # Retrieve the value for the selected combination of options
    value_Ke = values_Ke.get((Environment), "Not Found")

    # Update the value label with the retrieved value
    value_Ke_label.config(text=f"Ke: {value_Ke}")


# Button to retrieve the value for the selected options
get_value_button = tk.Button(root, text="Get Value", command=get_value_Ke)
get_value_button.pack()

# Label to display the value
value_Ke_label = tk.Label(root, text="")
value_Ke_label.pack()


root.mainloop()
