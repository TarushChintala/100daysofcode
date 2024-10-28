from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text='')
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Timer", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(10,countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += '✔'
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,24,"bold"))
timer_label.grid(row=0,column=1)


start_button = Button(text="Start",command= start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2,column= 2)


check_mark = Label(fg=GREEN, bg= YELLOW, font=(FONT_NAME,10))
check_mark.grid(row=3,column=1)



window.mainloop()