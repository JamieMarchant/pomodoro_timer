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
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    SHORT_BREAK_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(LONG_BREAK_sec)
        title_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Working Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor * REPS / 2):
            marks += "✔"
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomoto_img)
timer_text = canvas.create_text(
    100, 130, text=("00:00"), fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=2, row=2)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=2, row=1)

start_button = Button(
    text="Start", fg=GREEN, font=FONT_NAME, highlightthickness=0, command=start_timer
)
start_button.grid(column=1, row=3)

reset_button = Button(
    text="Reset", fg=GREEN, font=FONT_NAME, highlightthickness=0, command=reset_timer
)
reset_button.grid(column=3, row=3)

check_label = Label(text="✔", fg=GREEN, font=FONT_NAME, bg=YELLOW)
check_label.grid(column=2, row=4)


window.mainloop()
