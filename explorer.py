import tkinter
import os
from tkinter import filedialog


# Функция для выбора файла
def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(('Текстовый файл', '*.txt'),
                                                     ('Все файлы', '*')))
    if filename:
        text['text'] = text['text'] + ' ' + filename
        os.startfile(filename)


# Функция для отображения окна с информацией
def show_info():
    info_window = tkinter.Toplevel()
    info_window.title("Info")
    label = tkinter.Label(info_window, text="Как пользоваться блокнотом: \n 1. Выберите файл через 'Выбрать файл'."
                                            " \n 2. Откроется выбранный файл.")
    label.pack()


# Функция для отображения окна с информацией об авторе
def show_about():
    about_window = tkinter.Toplevel()
    about_window.title("About")
    label = tkinter.Label(about_window, text="Автор: Ваше Имя\nВерсия программы: 1.0")
    label.pack()


# Создание главного окна программы
window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x200')
window.configure(bg='black')
window.resizable(False, False)

# Добавление текста для отображения пути к файлу
text = tkinter.Label(window, text='Файл:', height=5, width=65, background='silver', foreground='blue')
text.grid(column=1, row=1)

# Кнопка для открытия проводника
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)

# Добавление меню
menubar = tkinter.Menu(window)

file_menu = tkinter.Menu(menubar, tearoff=0)
file_menu.add_command(label="Info", command=show_info)
file_menu.add_command(label="About", command=show_about)

menubar.add_cascade(label="Menu", menu=file_menu)
window.config(menu=menubar)

# Запуск главного цикла программы
window.mainloop()
