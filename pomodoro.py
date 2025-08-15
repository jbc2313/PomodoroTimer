# The program is going to allow you to enter the name of the task you are working on.
# Need to add to github
# its going to be a TKinter application

        
from tkinter import *
from tkinter import ttk


# still needs updated
def calculate(*args):
    try:
        value=float(feet.get())
        meters.set(int(0.308 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Pomodoro Timer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

init_time= StringVar() # used to be feet, I can delete this comment after I change every insance of feet
time_entry = ttk.Entry(mainframe, width=7, textvariable=init_time)
time_entry.grid(column=2, row=1, sticky=(W, E))

time_remaining = StringVar()
ttk.Label(mainframe, textvariable=time_remaining).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=(W))

ttk.Label(mainframe, text="The").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="remaining time is").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="seconds").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


time_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()

















# Enter name of task here


# Enter number of pomodoro cycles you want to go through
