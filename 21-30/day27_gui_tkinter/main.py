import tkinter
from tkinter.constants import X

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Label


my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
# my_label.pack()
# my_label.place(x=50, y=50)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
# or
# my_label.config(text="Another new text")


# Button


button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=2)

button2 = tkinter.Button(text="Click Me 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=10)
input.get()
# input.pack()
input.grid(column=3, row=3)

window.mainloop()
