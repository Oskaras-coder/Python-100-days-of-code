from tkinter import *




window = Tk()
window.title("Odilija smirda")
window.config(width=600, height=1000)


odilija = Label(text="ODILIJA", fg="green", font=("Times", 60, "bold"))
odilija.pack()

button = Button(text="Spausk jei esi Odilija")
button.pack()

window.mainloop()