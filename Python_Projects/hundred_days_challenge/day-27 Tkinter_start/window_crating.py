from tkinter import *

window = Tk()

window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("button clicked")


# Label

my_label = Label(text="I Am a Label", font=("Ariel", 24, "normal"))
my_label.grid(column=0, row=0) # svarbu, kad matytume kažką


# Button 1
button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)

# Button 2
button2 = Button(text="cllick maafee", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()