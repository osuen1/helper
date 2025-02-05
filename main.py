from tkinter import Tk, ttk

#TODO
# сделать контекстные подсказки по командам

root = Tk()

# размеры окна
root.geometry('700x100+400+200')
root.resizable(False, False)
root.attributes('-alpha', 0.9)

# поле ввода информации
text_area = ttk.Entry()
text_area.focus()
text_area.pack(fill='x', padx=20, pady=20)


if __name__ == '__main__':
    root.mainloop()