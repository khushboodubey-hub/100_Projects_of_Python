from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F875AA"
LIGHT_PINK = "#FDEDED"
GREEN = "#9bdeac"
BLUE = "#AEDEFC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfigure(timer_txt, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text=" ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg="red",  font=(FONT_NAME, 35))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg= "pink", font=(FONT_NAME, 35))
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg= PINK,  font=(FONT_NAME, 35))

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔️"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=LIGHT_PINK)


title_label = Label(text="Timer",fg=PINK, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=LIGHT_PINK, highlightthickness=0)
img = PhotoImage(file="Day_28/mine_own/bunny.png")
canvas.create_image(100, 112 , image = img)
timer_txt = canvas.create_text(127, 155, text="0", fill = "black", font=(FONT_NAME,8,"bold"))
canvas.grid(column=1, row=1)
# canvas.pack()

start_button = Button(text="Start", fg=PINK, bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=PINK, bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=BLUE, bg=LIGHT_PINK)
check_marks.grid(column=1, row=3)

# made it myself 

def do_nothing():
    messagebox.showinfo("Information", "you can't close the window until you click the close button !!")

window.protocol("WM_DELETE_WINDOW", do_nothing)

def to_close_window():
    window.destroy()

close_button = Button(text="Close", fg=PINK, bg="white", command=to_close_window)
close_button.grid(column=1, row=4)

window.mainloop()

