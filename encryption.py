choice = None
a='abcdefghijklmnopqrstuvwxyz'
while choice!='0':
    print(
        '''
1 - Ввод строки
2 - Настройка шифрующего алгоритма
3 - Шифрование строки, используя шифр Виженера
4 - Расшифорвание строки
0 - Выход из меню
''')
    choice = input('Выбор: ')
    if choice == '0':
        print('Выход')
    elif choice == '1':
        l = input('Введите строку: ')
        if l=='':
            print('Не введена строка')
        else:
            l=l.lower()
    elif choice == '2':
        key_word = input('Введите ключевое слово: ')
        if key_word=='':
            print('Не введено ключевое слово')
        else:
            key_word=key_word.lower()
    elif choice == '3':
        coded_word=''
        i=0
        for elem in l:
            if elem!=' ':
                coded_word+=a[(a.index(elem)+a.index(key_word[i%len(key_word)]))%26]
                i+=1
            else:
                coded_word+=' '
        print('Зашифрованная строка: ', coded_word)
    elif choice == '4':
        s=input('Введите строку: ')
        if s=='':
            print('Не введена строка')
        else:
            s=s.lower()
            key_word = input('Введите ключевое слово: ')
            if key_word=='':
                print('Не введена строка')
            else:
                key_word=key_word.lower()
                decoded_word=''
                i=0
                for elem in s:
                    if elem!=' ':
                        decoded_word+=a[(a.index(elem)-a.index(key_word[i%len(key_word)])+26)%26]
                        i+=1
                    else:
                        decoded_word+=' '
                print('Расшифровка строки: ', decoded_word)
