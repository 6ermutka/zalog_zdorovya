from tkinter import *
from tkinter import messagebox


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'»ћ“ = {bmi} соответствует недостаточному весу'
                                                f' ѕотребл€йте больше каллорий, белка. «анимайтесь спортом и бросьте вредные привычки.')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'»ћ“ = {bmi} соответствует нормальному весу'
                                                f' ¬ы молодцы, продолжайте в том же духе!')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'»ћ“ = {bmi} соответствует избыточному весу'
                                                f' ” вас не так все и плохо, но вам стоит пересмотреть свой образ жизни, подредактировать что-то в своем питании, начните вести подвижный образ жизни.')
    else:
        messagebox.showinfo('bmi-pythonguides', f'»ћ“ = {bmi} соответствует ожирению'
                                                f' ¬едите здоровый образ жизни и расcчитайте норму каллорий дл€ снижени€ веса.')


window = Tk()
window.title(' алькул€тор индекса массы тела (»ћ“)')
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="¬ведите свой рост (в см)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="¬ведите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='–ассчитать »ћ“',
    command=calculate_bmi
)
cal_btn.grid(row=5, column=2)

window.mainloop()