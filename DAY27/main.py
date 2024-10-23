from tkinter import *

def button_click():
    miles = float(input_entry.get())
    result = round(miles * 1.609)
    answer_label.config(text= f"{result}")


window = Tk()

window.title("Mile to Km Converter")
window.minsize(500,300)
window.config(padx= 125,pady=100)

miles_label = Label(text="Miles",font= ("Arial",10))
miles_label.grid(row= 0, column= 2)

km_label = Label(text="Km",font= ("Arial",10))
km_label.grid(row= 1, column= 2)

equal_label = Label(text="is equal to",font= ("Arial",10))
equal_label.grid(row= 1, column= 0)

input_entry = Entry()
input_entry.insert(0,"0")
input_entry.grid(row= 0, column= 1)

calc_button = Button(text="Calculate",command= button_click,font= ("Arial",10))
calc_button.grid(row=2, column=1)

answer_label = Label(text= "0",font= ("Arial",10))
answer_label.grid(row= 1, column= 1)












window.mainloop()