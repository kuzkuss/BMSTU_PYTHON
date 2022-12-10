from tkinter import *
from tkinter import messagebox as box

#Функция ввода цифры
def add_digit(digit):
    global n1
    value = calc.get()
    if value[-1] in '-+' and len(value) != 1:
        calc.delete(0, END)
        calc.insert(0, digit)
        n1 = value
    elif value[0] == '0' and digit != '.' and len(value) == 1:
        calc.delete(0, END)
        calc.insert(0, digit)
    else:
        calc.insert(END, digit)

#Функция ввода операции   
def add_operation(oper):
    global f
    f += 1
    value = calc.get()
    if value[-1] in '-+':
        value = value[:-1]
    elif f > 1:
        calculate()
        n1 = calc.get()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + oper)

#Функции операций
def diff(n1, n2):
    n = 0
    k = 0
    count = 0
    k2 = 0
    while (n1 * 10 % 10 != 0) or (n2 * 10 % 10 != 0):
        n1 *= 10
        n2 *= 10
        k += 1
    if n1 < n2:
        while n1 > 0 or n2 > 0:
            if n2 % 10 - k2 < n1 % 10:
                n += (n2 % 10 + 4 - k2 - n1 % 10) % 4 * 10**count
                k2 = 1
            else:
                n += (n2 % 10 - k2 - n1 % 10) % 4 * 10**count
                k2 = 0
            count += 1
            n1 //= 10
            n2 //= 10
        return -n / 10**k
    else:
        while n1 > 0 or n2 > 0:
            if n1 % 10 - k2 < n2 % 10:
                n += (n1 % 10 + 4 - k2 - n2 % 10) % 4 * 10**count
                k2 = 1
            else:
                n += (n1 % 10 - k2 - n2 % 10) % 4 * 10**count
                k2 = 0
            count += 1
            n1 //= 10
            n2 //= 10
        return n / 10**k
    
def summ(n1, n2):
    count = 0
    k = 0
    n = 0
    while (n1 * 10 % 10 != 0) or (n2 * 10 % 10 != 0):
        n1 *= 10
        n2 *= 10
        k += 1
    while n1 > 0 or n2 > 0:
        if n1 % 10 + n2 % 10 + n//10**count >= 4:
            q = n1 % 10 + n2 % 10 + n//10**count
            n -= (n//10**count) * 10**count
            n += q % 4 * 10**count
            count += 1
            n += q // 4 * 10**count
        else:    
            n += (n1 % 10 + n2 % 10 ) % 4 * 10**count
            count += 1
            n += (n1 % 10 + n2 % 10) // 4 * 10**count
        n1 //= 10
        n2 //= 10
    return n / 10**k

#Функция, производящая вычисления
def calculate():
    global n1
    n2 = calc.get()
    if n2[-1] == '-':
        if n2[0] == '-':
            n2 = float(n2[1:-1])
            n = diff(n2, n2)
        else:
            n2 = float(n2[:-1])
            n = diff(n2, n2)
    elif n2[-1] == '+':
        if n2[0] == '-':
            n2 = float(n2[1:-1])
            n = -summ(n2, n2)
        else:
            n2 = float(n2[:-1])
            n = summ(n2, n2)
    elif n1[-1] == '+':
        if n1[0] == '-' and n2[0] == '-':
            n1 = float(n1[1:-1])
            n2 = float(n2[1:])
            n = -summ(n1, n2)
        elif n1[0] == '-' and n2[0] != '-':
            n1 = float(n1[1:-1])
            n2 = float(n2)
            n = diff(n2, n1)
        elif n1[0] != '-' and n2[0] == '-':
            n1 = float(n1[:-1])
            n2 = float(n2[1:])
            n = diff(n1, n2)
        else:
            n1 = float(n1[:-1])
            n2 = float(n2)
            n = summ(n1, n2)
    elif n1[-1] == '-':
        if n1[0] == '-' and n2[0] == '-':
            n1 = float(n1[1:-1])
            n2 = float(n2[1:])
            n = diff(n2, n1)
        elif n1[0] == '-' and n2[0] != '-':
            n1 = float(n1[1:-1])
            n2 = float(n2)
            n = -summ(n2, n1)
        elif n1[0] != '-' and n2[0] == '-':
            n1 = float(n1[:-1])
            n2 = float(n2[1:])
            n = summ(n1, n2)
        else:
            n1 = float(n1[:-1])
            n2 = float(n2)
            n = diff(n1, n2)
    calc.delete(0, END) 
    calc.insert(0, n)
    n1 = str(n)

#Функция смены знака
def change_sign():
    value = calc.get()
    if value[0] == '-':
        value = value[1:]
    else:
        value = '-' + value
    calc.delete(0, END)
    calc.insert(0, value)
    
#Функция очищения поля ввода
def clear():
    global f
    f = 0
    calc.delete(0, END)
    calc.insert(0, '0')

#Функции создания кнопок
def make_button(digit):
    return Button(text = digit, bd = 4, font = ('Arial', 13), command = lambda : add_digit(digit))

def make_info():
    return Button(text = 'INFO', bd = 4, font = ('Arial', 13), command = info)

def operation(oper):
    return Button(text = oper, bd = 4, font = ('Arial', 13), command = lambda : add_operation(oper))

def calculation(oper):
    return Button(text = oper, bd = 4, font = ('Arial', 13), command = calculate)

def del_button(oper):
    return Button(text = oper, bd = 4, font = ('Arial', 13), command = clear)

def sign_button(sign):
    return Button(text = sign, bd = 4, font = ('Arial', 13), command = change_sign)

#Реализация ввода с клавиатуры
def input_keyboard(event):
    if event.char in ['0', '1', '2', '3', '.', '-']:
        add_digit(event.char)
    elif (event.char == '-' or event.char == '+') and calc.get != '':
        add_operation(event.char)
    elif event.char == '\r' or event.char == '=':
        calculate()
    elif event.char == '':
        clear()
    else:
        box.showinfo('Attention!', 'You should input only digits or operations.')

#Information
def info():
    box.showinfo('Information', '''Сложение и вычитание в 4СС
Кузнецова Анастасия ИУ7-21Б''')

#Создание основного окна
root = Tk()
root.geometry('180x270+100+200')
root.config(bg = 'black')
root.title('Калькулятор')
f = 0

root.bind('<Key>', input_keyboard)

#Создание поля ввода
calc = Entry(root, justify = RIGHT, font = ('Arial', 15), width = 10)
calc.insert(0, '0')
calc.grid(row = 0, column = 0, columnspan = 3, stick = 'we', padx = 5)

#Создание и размещение кнопок
make_button('1').grid(row = 2, column = 0, stick = 'wens', pady = 5, padx = 5)
make_button('2').grid(row = 2, column = 1, stick = 'wens', pady = 5, padx = 5)
make_button('3').grid(row = 3, column = 0, stick = 'wens', pady = 5, padx = 5)
make_button('0').grid(row = 3, column = 1, stick = 'wens', pady = 5, padx = 5)
make_button('.').grid(row = 4, column = 0, stick = 'wens', pady = 5, padx = 5)

make_info().grid(row = 4, column = 1, columnspan = 2, stick = 'wens', pady = 5, padx = 5)

operation('+').grid(row = 1, column = 2, stick = 'wens', pady = 5, padx = 5)
operation('-').grid(row = 2, column = 2, stick = 'wens', pady = 5, padx = 5)

calculation('=').grid(row = 3, column = 2, stick = 'wens', pady = 5, padx = 5)
del_button('C').grid(row = 1, column = 0, stick = 'wens', pady = 5, padx = 5)
sign_button('+/-').grid(row = 1, column = 1, stick = 'wens', pady = 5, padx = 5)

root.grid_columnconfigure(0, minsize = 60)
root.grid_columnconfigure(1, minsize = 60)
root.grid_columnconfigure(2, minsize = 60)

root.grid_rowconfigure(1, minsize = 60)
root.grid_rowconfigure(2, minsize = 60)
root.grid_rowconfigure(3, minsize = 60)
root.grid_rowconfigure(4, minsize = 60)

#Создание меню
mainmenu = Menu(root)
root.config(menu = mainmenu)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu2 = Menu(filemenu, tearoff = 0)

filemenu2.add_command(label = '+', command = lambda : add_operation('+'))
filemenu2.add_command(label = '-', command = lambda : add_operation('-'))

filemenu.add_command(label = 'Clear', command = clear)
filemenu.add_cascade(label = 'Determined actions', menu = filemenu2)

mainmenu.add_cascade(label = 'File', menu = filemenu)
mainmenu.add_command(label = 'Info', command = info)

root.mainloop()
