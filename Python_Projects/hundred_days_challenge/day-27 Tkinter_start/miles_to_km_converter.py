from tkinter import *

window = Tk()

# Window

window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    new_text = entry.get()
    new_text = round(int(new_text) * 1.61, 2)
    miles.config(text=new_text)


# Label miles to km calculation

miles = Label(text="0", font=("Ariel", 12, "normal"))
miles.grid(column=1, row=1)

equal = Label(text="is equal to", font=("Ariel", 12, "normal"))
equal.grid(column=0, row=1)

text_miles = Label(text="Miles", font=("Ariel", 12, "normal"))
text_miles.grid(column=2, row=0)

Km = Label(text="Km", font=("Ariel", 12, "normal"))
Km.grid(column=2, row=1)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

#Entries
entry = Entry(width=10)
entry.grid(column=1, row=0)


window.mainloop()
