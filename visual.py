from tkinter import Tk, ttk
import functions as f
import keyboard

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

keyboard.add_hotkey('f1+enter', lambda: f.cache(text_area.get()))

root.mainloop()