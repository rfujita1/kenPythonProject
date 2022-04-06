from tkinter import *

main_window = Tk()

# Label(main_window, text="Enter name").grid(row=0, column=0)

# Label(main_window, text= "what ur age?").grid(row =1, column=0)

# my_name = Entry(main_window, width=50, borderwidth=5)
# my_name.grid(row=0, column=1)

# my_age=Entry(main_window, width=50, borderwidth=5)
# my_age.grid(row=1, column=1)
def func(args):
    print(args)
Button(main_window, text="CONFERENCE_NAME", command=lambda: func("CONFERENCE_NAME"), width =50).grid(row=2, column=1)
Button(main_window, text="CONFERENCE_NAME", command=lambda: func("CONFERENCE_NAME"), width =50).grid(row=3, column=1)
Button(main_window, text="CONFERENCE_NAME", command=lambda: func("CONFERENCE_NAME"), width =50).grid(row=4, column=1)

main_window.mainloop()

