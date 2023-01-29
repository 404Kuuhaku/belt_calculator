import math
import tkinter as tk
from tkinter import ttk

def calculate():
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
    Running_time = float(Running_time_entry.get())
    Environment = int(Environment_entry.get())





# Create the main window
root = tk.Tk()
root.title("Calculator")

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

Running_time_label = ttk.Label(input_frame, text="Enter a value for Running time(hr/day):")
Running_time_label.grid(row=5, column=0)
Running_time_entry = ttk.Entry(input_frame)
Running_time_entry.grid(row=5, column=1)

Environment_label = ttk.Label(input_frame, text="Enter a value for Environment:")
Environment_label.grid(row=6, column=0)
Environment_entry = ttk.Entry(input_frame)
Environment_entry.grid(row=6, column=1)





# Create a button to initiate the calculation
calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate)
calculate_button.grid(row=7, column=0, columnspan=2, pady=10)


# Create a label to display the result

result_label = tk.Label(input_frame)
result_label.grid(row=8, column=0, columnspan=2)


SR_label = ttk.Label(input_frame)
SR_label.grid(row=9, column=0, columnspan=2)


L_label = ttk.Label(input_frame)
L_label.grid(row=10, column=0, columnspan=2)

root.mainloop()