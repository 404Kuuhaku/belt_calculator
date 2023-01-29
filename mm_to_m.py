import tkinter as tk
from tkinter import ttk

def convert():
    value = float(input_value.get())
    if input_unit.get() == "mm":
        output_value.set(value/1000)
        output_unit.set("m")
    else:
        output_value.set(value*1000)
        output_unit.set("mm")


root = tk.Tk()
root.title("Length Converter")

input_value = tk.StringVar()
output_value = tk.StringVar()
output_unit = tk.StringVar()

input_frame = ttk.Frame(root)
input_frame.pack()

input_label = ttk.Label(input_frame, text="Value:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = ttk.Entry(input_frame, textvariable=input_value)
input_entry.grid(row=0, column=1, padx=5, pady=5)

input_unit = tk.StringVar()
input_unit.set("mm")

input_unit_mm = ttk.Radiobutton(input_frame, text="mm", variable=input_unit, value="mm")
input_unit_mm.grid(row=0, column=2, padx=5, pady=5)

input_unit_m = ttk.Radiobutton(input_frame, text="m", variable=input_unit, value="m")
input_unit_m.grid(row=0, column=3, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.pack()

output_frame = ttk.Frame(root)
output_frame.pack()

output_label = ttk.Label(output_frame, textvariable=output_value)
output_label.grid(row=0, column=0, padx=5, pady=5)

output_unit_label = ttk.Label(output_frame, textvariable=output_unit)
output_unit_label.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
