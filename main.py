from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
# Colours: https://colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
countdown = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(countdown)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Pop up when changing
    window.attributes("-topmost", True)
    window.attributes("-topmost", False)
    if reps % 2 == 1:
        # green
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        # red
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        # pink
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# GUIs are event driven, meaning always checking for things
def count_down(count):
    global reps, checkmarks, countdown
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        countdown = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# Tomato in Italian
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# 103 not 100 because it's slightly shifted
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40))
canvas.grid(column=1, row=1)

# Timer
timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmarks
checkmarks = Label(text="", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

# Hints for Labels
# 1. fg = foreground
# 2. copy checkmark symbol: text="checkmark"
# 3. use grid() instead of pack. 4 rows, 3 columns




window.mainloop()





