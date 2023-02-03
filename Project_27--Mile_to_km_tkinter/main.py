from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=200)
window.config(padx=40, pady=40)

new_entry = Entry(width=10)
new_entry.grid(column=1, row=0)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)
my_label.config(padx=10, pady=10)

my_label_1 = Label(text="is equal to")
my_label_1.grid(column=0, row=1)
my_label.config(padx=10, pady=10)


def converter():
    value = round(float(new_entry.get()) * 1.6)
    my_label_2.config(text=str(value))


my_label_2 = Label(text=0)
my_label_2.grid(column=1, row=1)
my_label_2.config(padx=10, pady=10)

my_label_3 = Label(text="Km")
my_label_3.grid(column=2, row=1)
my_label_3.config(padx=10, pady=10)

new_button = Button(text="Calculate", command=converter)
new_button.grid(column=1, row=2)
new_button.config(padx=10, pady=10)

window.mainloop()
