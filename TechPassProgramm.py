import os
import tkinter as tk
from tkinter import messagebox
import itertools

root = tk.Tk()
root.title('')
root.geometry('175x35')
root.resizable(False, False)


directories = [''] # place a list of directories here

output = {}


def passports_in_directories():
    """This func creates a dictionary with folder as key and a list of passports as value. """
    for directory in directories:
        directory_name = directory.split('//')[-1]
        files = os.listdir(directory)

        passport_files = []
        for file in files:
            if file.startswith('Паспорт'):
                passport_files.append(file)

            passport_numbers = []
            for passport in passport_files:
                number_without_extension = passport.split('.')[0]
                number_of_line_and_passport = number_without_extension.split()[2:]
                full_passport_number = '\t'.join(number_of_line_and_passport)
                passport_numbers.append(full_passport_number)
                output[directory_name] = passport_numbers
    return output


def check_passports():
    """This is the main func, which writes the output to txt file."""
    passports_in_directories()
    check_double_passports()
    try:
        os.remove('') # here shall be the pass to txt. file with status of docs
    except OSError:
        pass

    with open('', 'w') as f: # same path as above to create a txt. file with status of docs
        for key, value in output.items():
            values = [v for v in value]
            f.write('%s(%d):\n%s\n' % (key, len(values), "\n".join(values)))


def check_double_passports():
    """This func first flattens the lists and then checks, if any passports are doubled and writes to txt."""
    root.destroy()
    doubled_passports = {}
    list_of_lists = [value for value in output.values()]
    flat_list = list(itertools.chain(*list_of_lists))

    list_to_check_doubles = []
    for item in flat_list:
        number_in_brackets = item.split()[1]
        list_to_check_doubles.append(number_in_brackets)
        count_of_appearance = list_to_check_doubles.count(number_in_brackets)
        if count_of_appearance > 1:
            doubled_passports[number_in_brackets] = count_of_appearance

    if doubled_passports:
        messagebox.showwarning(title='Внимание!', message='Найдены дублированные паспорта!')
        try:
            os.remove('') # here shall be the pass to txt. file with doubled docs
        except OSError:
            pass

        with open('', 'w') as f: # same path as above to create a txt. file with doubled docs
            for key, value in doubled_passports.items():
                f.write('%s --> %s\n' % (key, value))
    else:
        message_with_passport_numbers = f"Нет дублированных паспортов.\nВсего: {len(flat_list)}."
        messagebox.showinfo(title='Для инфо', message=message_with_passport_numbers)


starter_button = tk.Button(root, bg='#5F6161', fg='#F8FCFC', text='! ПРОВЕРИТЬ ПАСПОРТА !', command=check_passports)
starter_button.place(relx=.5, rely=.5, anchor=tk.CENTER)

root.mainloop()
