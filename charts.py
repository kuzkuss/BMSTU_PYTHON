import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin
plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()

#Диапазон значений
x = np.linspace(-10, 10, 10000)
y1 = np.sin(x)
y2 = x * np.cos(x)

#Построение графиков
ax.plot(x, y1, c = 'blue', ls = '--', linewidth = 2, label = '$y = sin(x)$')
ax.plot(x, y2, c = 'g', ls = '-', alpha = 1, label = '$y = x*cos(x)$')

#Поиск корней первой функции
flag = 0
for i in range (len(x) - 1):
    if flag == 0:
        if y1[i] * y1[i + 1] < 0:
            ax.scatter(x[i], y1[i], color='orange',
                       s=30, marker='o', label = 'Корни')
            flag = 1
    else:
        if y1[i] * y1[i + 1] < 0:
            ax.scatter(x[i], y1[i], color='orange', s=30, marker='o')

#Поиск экстремумов первой функции
flag = 0
for i in range (1, len(x) - 1):
    if flag == 0:
        if y1[i - 1] < y1[i] > y1[i + 1]:
            ax.scatter(x[i], y1[i], color='red',
                       s=30, marker='o', label = 'Максимальные точки экстремума')
            flag = 1
    else:
        if y1[i - 1] < y1[i] > y1[i + 1] or y1[i - 1] > y1[i] < y1[i + 1]:
            ax.scatter(x[i], y1[i], color='red', s=30, marker='o')

flag = 0
for i in range (1, len(x) - 1):
    if flag == 0:
        if y1[i - 1] > y1[i] < y1[i + 1]:
            ax.scatter(x[i], y1[i], color='purple',
                       s=30, marker='o', label = 'Минимальные точки экстремума')
            flag = 1
    else:
        if y1[i - 1] > y1[i] < y1[i + 1] or y1[i - 1] > y1[i] < y1[i + 1]:
            ax.scatter(x[i], y1[i], color='purple', s=30, marker='o')

#Поиск максимума функции
y1max = max(y1)
y2max = max(y2)
y1min = min(y1)
y2min = min(y2)
flag = 0
for y in y1:
    if flag == 0:
        if y == y1max:
            ax.scatter(x[i], y1[i], color='yellow',
                       s=30, marker='o', label = 'Максимум функции')
            flag = 1
    else:
        if y == y1max:
            ax.scatter(x[i], y1[i], color='yellow', s=30, marker='o')

for y in y2:
    if y == y2max:
        ax.scatter(x[i], y1[i], color='yellow', s=30, marker='o')

#Поиск минимума функции        
flag = 0
for y in y1:
    if flag == 0:
        if y == y1min:
            ax.scatter(x[i], y1[i], color='violet',
                       s=30, marker='o', label = 'Минимум функции')
            flag = 1
    else:
        if y == y1min:
            ax.scatter(x[i], y1[i], color='violet', s=30, marker='o')

for y in y2:
    if y == y2min:
        ax.scatter(x[i], y1[i], color='violet', s=30, marker='o')
            
#Поиск корней второй функции            
for i in range (len(x) - 1):
    if y2[i] * y2[i + 1] < 0:
        ax.scatter(x[i], y2[i], color='orange', s=30, marker='o')

#Поиск экстремумов второй функции
for i in range (1, len(x) - 1):
    if y2[i - 1] < y2[i] > y2[i + 1]:
        ax.scatter(x[i], y2[i], color='red', s=30, marker='o')
    elif y2[i - 1] > y2[i] < y2[i + 1]:
        ax.scatter(x[i], y2[i], color='purple', s=30, marker='o')

#Поиск точек перегиба
def f2_2(x):
    return -2 * sin(x) - x * cos(x)
flag = 0
for i in range (len(x) - 1):
    if flag == 0:
        if f2_2(x[i]) * f2_2(x[i + 1]) < 0 and f2_2(x[i]) == 0:
            ax.scatter(x[i], y2[i], color='black',
                       s=30, marker='o', label = 'Точки перегиба')
            flag = 1
    else:
        if f2_2(x[i]) * f2_2(x[i + 1]) < 0 and f2_2(x[i]) == 0:
            ax.scatter(x[i], y2[i], color='black', s=30, marker='o')

def f1_2(x):
    return -sin(x)

for i in range (len(x) - 1):
        if f1_2(x[i]) * f1_2(x[i + 1]) < 0 and f1_2(x[i]) == 0:
            ax.scatter(x[i], y1[i], color='black', s=30, marker='o')

#Заголовок и подписи осей
ax.set_title('$Matplotlib$', fontsize = 20)
ax.set_xlabel('$Ось X$')
ax.set_ylabel('$Ось Y$')

ax.legend(loc = 'best')

plt.show()
