from tkinter import *
FONT = ("Arial", 12)


window = Tk()
window.minsize(width= 300, height=150)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)


entry = Entry(width=10)
entry.grid(column=2, row=0)
entry.get()


label1 = Label(text="Miles", font=FONT)
label1.grid(column=3, row=0)


label2 = Label(text="is equal to", font=FONT)
label2.grid(column=1, row=1)

label3 = Label(text="0", font=FONT)
label3.grid(column=2, row=1)

label4 = Label(text="Km", font=FONT)
label4.grid(column=3, row=1)

def conversion():
    mile = float(entry.get())
    new_text = mile*1.6093
    label3.config(text = new_text)

button = Button(text ="Calculate", command=conversion)
button.grid(column=2, row=3)








window.mainloop()




