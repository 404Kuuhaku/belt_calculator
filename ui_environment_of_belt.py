import tkinter as tk
from tkinter import ttk

def on_select(v):
    value = values[v]
    label.config(text=f"Value for {options[v]} is {value}")

root = tk.Tk()
root.geometry("300x200")

options = {
    1: "Normal Environment",
    2: "Frequent start and stop of machine",
    3: "Hard to conduct maintenance checkup",
    4: "Dusty environment",
    5: "High temperature",
    6: "Oil or water splashing",
}

values = {
    1: 0,
    2: 0.2,
    3: 0.2,
    4: 0.2,
    5: 0.2,
    6: 0.2,
}

var = tk.StringVar(value='Select an Environment')
dropdown = tk.OptionMenu(root, var, *options, command=lambda v: on_select(int(v)))
dropdown.pack()

label = tk.Label(root, text="")
label.pack()



table = ttk.Treeview(root, columns=("NO.", "Environment", "Value"))
table.heading("NO.", text="NO.")
table.heading("Environment", text="Environment")
table.heading("Value", text="Value")
table.insert("", 0, values=("1", "Normal Environment", "0.2"))
table.insert("", 1, values=("2", "Frequent start and stop of machine","0.2"))
table.insert("", 2, values=("3", "Hard to conduct maintenance checkup", "0.2"))
table.insert("", 3, values=("4", "Dusty environment", "0.2"))
table.insert("", 4, values=("5", "High temperature", "0.2"))
table.insert("", 5, values=("1", "Oil or water splashing", "0.2"))

table.pack()




root.mainloop()