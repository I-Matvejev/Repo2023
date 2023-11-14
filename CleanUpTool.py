import os
import shutil
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('CleanUpTool')
root.geometry('300x85')
root.resizable(False, False)

path_entry = tk.Entry(root, width=47)
path_entry.focus_set()
path_entry.place(x=5, y=30)


def are_you_sure():
    MsgBox = tk.messagebox.askquestion('Clean UP', 'Вы уверены, что хотите сортировать файлы?',
                                       icon='warning')
    if MsgBox == 'yes':
        pass
    else:
        root.destroy()


def clean_up_command():
    exclude = ['Thumbs.db', '.tmp']
    path = str(path_entry.get())

    are_you_sure()

    if os.path.exists(path + '/' + 'В этой папке.txt'):
        os.remove(path + '/' + 'В этой папке.txt')

    filenames = os.listdir(path)

    for file_ in filenames:

        name, ext = os.path.splitext(file_)
        ext = ext[1:]

        if ext == '':
            continue

        if os.path.exists(path + '/' + ext):
            shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)
        else:
            os.makedirs(path + '/' + ext)
            shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

    with open(path + '/' + 'В этой папке.txt', 'w', encoding='utf-8') as txtfile:
        for path, dirs, files in os.walk(path):
            sep = "\n---------- " + path.split("\\")[len(path.split("\\")) - 1] + " ----------"
            txtfile.write(f"{sep}\n")

            for fn in sorted(files):
                if not any(x in fn for x in exclude):
                    filename = os.path.splitext(fn)[0]
                    txtfile.write(f"{filename}\n")

    os.startfile(path)


clean_up_button = tk.Button(root, bd=5, text='Clean Up', command=clean_up_command)
clean_up_button.pack(side=tk.BOTTOM)

path_label = tk.Label(root, text='Введите путь к директории для сортировки:')
path_label.place(x=5, y=5)

root.mainloop()
