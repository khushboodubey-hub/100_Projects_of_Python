from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)
window.config(padx=20, pady=20)

# Lable
my_label = Label(text="I'm a Label.", font=("Ariel", 15, "italic"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()




