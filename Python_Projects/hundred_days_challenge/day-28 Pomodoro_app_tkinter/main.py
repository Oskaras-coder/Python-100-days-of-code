from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer) # cancel the timer
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
    global checkmarks
    checkmarks = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checkmarks
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += 1
            checkmark_label.config(text=checkmarks*"✔")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas widget, you can put things one on top of the other

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


button1 = Button(text="Start", command=start_timer, highlightthickness=0)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark_label = Label(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)
# text="✔",
window.mainloop()