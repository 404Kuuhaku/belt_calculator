import tkinter as tk

def on_select(v):
    value = values[v]
    label.config(text=f"Value for {options[v]} is {value}")

root = tk.Tk()
root.geometry("300x200")

options = {
    1: "Frequent start and stop of machine",
    2: "Hard to conduct maintenance checkup",
    3: "Dusty environment",
    4: "High temperature",
    5: "Oil or water splashing",
}

values = {
    1: 0.1,
    2: 0.2,
    3: 0.3,
    4: 0.4,
}

var = tk.StringVar(value='Select an option')
dropdown = tk.OptionMenu(root, var, *options, command=lambda v: on_select(int(v)))
dropdown.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
