import pickle
def create_database():
    base_name = input('Введите название базы данных: ')
    base_list.append(base_name)
    f = open(rf'G:\Универ\{base_name}.txt', 'wb')
    count_rows = int(input('Введите количество полей: '))
    rows = []
    print('Введите поля:')
    for i in range(count_rows):
        rows.append(input())
    database = {0:rows}
    pickle.dump(database,f)
    f.close()

def add_to_database():
    if base_list == []:
        print('Нет созданных баз данных')
    else:
        print('Выберите базу данных из списка: ')
        for x in base_list:
            print(x)
        choice_base = input()
        f = open(rf'G:\Универ\{choice_base}.txt', 'rb')
        choice_database = pickle.load(f)
        f.close()
        for i,j in enumerate (choice_database[0]):
            print(i+1, '-',j)
        print('Введите новые поля: ')
        new_stroke =[]
        for i in range(len(choice_database[0])):
            new_stroke.append(input())
        choice_database[len(choice_database)] = new_stroke
        f = open(rf'G:\Универ\{choice_base}.txt', 'wb')
        pickle.dump(choice_database,f)
        f.close()
        
def print_database():
    if base_list == []:
        print('Нет созданных баз данных')
    else:
        print('Выберите базу данных из списка: ')
        for x in base_list:
            print(x)
        choice_base = input()
        f = open(rf'G:\Универ\{choice_base}.txt', 'rb')
        choice_database = pickle.load(f)
        f.close()
        n = len(choice_database[0])
        max_len = [0]*n
        n2 = len(choice_database)
        for i in range(n2):
            for j in range(n):
                if len(choice_database[i][j]) > max_len[j]:
                    max_len[j] = len(choice_database[i][j])
        stroke1 = '┌─────┬' + '┬'.join((x+2)*'─' for x in max_len) + '┐'
        stroke = '├─────┼' + '┼'.join((x+2)*'─' for x in max_len) + '┤'
        print(stroke1)
        for i in range (n2):
            print('│',end='')
            if i == 0:
                print(' Код │', end='')
            else:
                print(' {:^3} │'.format(i), end='')
            for j in range (n):
                print(' {:^{}} │'.format(choice_database[i][j], max_len[j]),end='')
            print()
            if i != n2-1:
                print(stroke)
        end_stroke = stroke1.replace('┬','┴').replace('┌','└').replace('┐','┘')
        print(end_stroke)
            
def search1():
    if base_list == []:
        print('Нет созданных баз данных')
    else:
        print('Выберите базу данных из списка: ')
        for x in base_list:
            print(x)
        choice_base = input()
        f = open(rf'G:\Универ\{choice_base}.txt', 'rb')
        choice_database = pickle.load(f)
        f.close()
        print('Введите поле для поиска из списка: ')
        for i in (choice_database[0]):
            print(i)
        choice_row = input()
        print('Введите значение этого поля для поиска')
        choice_v = input()
        print('Найденные записи: ')
        for i in range(len(choice_database)):
            if choice_v == choice_database[i][choice_database[0].index(choice_row)]:
                print(*choice_database[i])
        
def search2():
    if base_list == []:
        print('Нет созданных баз данных')
    else:
        print('Выберите базу данных из списка: ')
        for x in base_list:
            print(x)
        choice_base = input()
        f = open(rf'G:\Универ\{choice_base}.txt', 'rb')
        choice_database = pickle.load(f)
        f.close()
        print('Введите поля для поиска из списка: ')
        for i in (choice_database[0]):
            print(i)
        choice_row1 = input()
        choice_row2 = input()
        print('Введите значения этих полей для поиска')
        choice_v1 = input()
        choice_v2 = input()
        print('Найденные записи: ')
        for i in range(len(choice_database)):
            if choice_v1 == choice_database[i][choice_database[0].index(choice_row1)] and choice_v2 == choice_database[i][choice_database[0].index(choice_row2)]:
                print(*choice_database[i])

base_list = []
choice = None
while choice != '0':
    print(
        '''
1 - Создание БД.
2 - Добавление записи в БД.
3 - Вывод всей БД.
4 - Поиск записи по одному полю.
5 - Поиск записи по двум полям.
0 - Выход из меню
''')
    choice = input('Выбор: ')
    if choice == '0':
        print('Выход')
    elif choice == '1':
        create_database()
    elif choice == '2':
        add_to_database()
    elif choice == '3':
        print_database()
    elif choice == '4':
        search1()
    elif choice == '5':
        search2()