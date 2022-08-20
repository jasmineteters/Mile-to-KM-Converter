from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

is_equal_to = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(pady=10, padx=10)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(pady=10, padx=10)

km_label = Label(text="KM", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)
km_label.config(pady=10, padx=10)

answer_label = Label(text="0", font=("Arial", 24, "bold"))
answer_label.grid(column=1, row=1)



#Button
def button_clicked():
    miles_to_calc = float(miles_input.get())
    answer = round((miles_to_calc * 1.6), 1)
    answer_label.config(text=f"{answer}")


button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)


#Input

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


window.mainloop()