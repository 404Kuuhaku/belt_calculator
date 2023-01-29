import math
import tkinter as tk

def on_submit():
    D = float(D_entry.get())
    d = float(d_entry.get())
    C = float(C_entry.get())

    if (D+d)/2 < C:
        result_label.config(text="Distance between centers of pulley is ok")
    else:
        result_label.config(text="Distance between centers of pulley is too short")

# Create a new Tkinter window
root = tk.Tk()
root.title("SR and L Calculator")

# Create labels for the input fields
D_label = tk.Label(root, text="Enter a value for D(inch):")
D_label.pack()

d_label = tk.Label(root, text="Enter a value for d(inch):")
d_label.pack()

C_label = tk.Label(root, text="Enter a value for C(inch):")
C_label.pack()

# Create entry fields for the input values
D_entry = tk.Entry(root)
D_entry.pack()

d_entry = tk.Entry(root)
d_entry.pack()

C_entry = tk.Entry(root)
C_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
