def left_side():
    for i in range(n):
        print('{:<150}'.format(text[i]))

def right_side():
    for i in range(n):
        print('{:>150}'.format(text[i]))

def width():
    for x in text:
        if x!='':
            s = x.split()
            if len(s)>1:
                k = -len(s)+1
                j = 0
                while k != max_len - len(x):
                    s[j] += ' '
                    k += 1
                    j = k%(len(s)-1)
                s = ''.join(s)
                print(s)
            else:
                print(x)

def delete_word():
    word = input('Введите слово, которое нужно удалить: ')
    for x in text:
        x = x.replace(word+',','')
        x = x.replace(word+'.','')
        x = x.replace('"'+word+'"','')
        x = x.replace(word,'')
        print(x)

def replace_word():
    word = input('Введите слово, которое надо заменить: ')
    new_word = input('Введите новое слово, на которое надо заменить: ')
    for i in range(n):
        text[i] = text[i].replace(word,new_word)
        print(text[i])
def calculation_1(z):
    z = z.replace(' ','')
    z = z.replace('--','+')
    z = z.replace('+-','-')
    if len(z)>2:
        value=[z[0]]
        for i in z[1:]:
            if i.isdigit():
                value[-1]+=i
            else:
                value.append(i)
                value.append('')
        value='A'+'A'.join(value)+'A'
        operator = '^'
        for i in range (value.count(operator)):
            first_digit = value[value[:value.index(operator)-1].rfind('A')+1:value.index(operator)-1]
            second_digit = value[value.index(operator)+2:value.index(operator)+2+value[value.index(operator)+2:].find('A')]
            c_res = float(first_digit)**float(second_digit)
            value=value.replace(first_digit+'A'+operator+'A'+second_digit,str(c_res))
        
        for i in value:
            if i == '*':
                operator = '*'
                first_digit = value[value[:value.index(operator)-1].rfind('A')+1:value.index(operator)-1]
                second_digit = value[value.index(operator)+2:value.index(operator)+2+value[value.index(operator)+2:].find('A')]
                c_res = float(first_digit)*float(second_digit)
                value=value.replace(first_digit+'A'+operator+'A'+second_digit,str(c_res))
            if i == '/':
                operator = '/'
                first_digit = value[value[:value.index(operator)-1].rfind('A')+1:value.index(operator)-1]
                second_digit = value[value.index(operator)+2:value.index(operator)+2+value[value.index(operator)+2:].find('A')]
                c_res = float(first_digit)/float(second_digit)
                value=value.replace(first_digit+'A'+operator+'A'+second_digit,str(c_res))
        operator = '+'
        for i in range (value.count(operator)):
            first_digit = value[value[:value.index(operator)-1].rfind('A')+1:value.index(operator)-1]
            second_digit = value[value.index(operator)+2:value.index(operator)+2+value[value.index(operator)+2:].find('A')]
            c_res = float(first_digit)+float(second_digit)
            value=value.replace(first_digit+'A'+operator+'A'+second_digit,str(c_res))
        operator = '-'
        for i in range (value.count(operator)):
            index = value.find('-')
            if value[index+1] == 'A':
                first_digit = value[value[:value.index(operator)-1].rfind('A')+1:value.index(operator)-1]
                second_digit = value[value.index(operator)+2:value.index(operator)+2+value[value.index(operator)+2:].find('A')]
                c_res = float(first_digit)-float(second_digit)
                value=value.replace(first_digit+'A'+operator+'A'+second_digit,str(c_res))
        value=value.replace('A','')
        return str(round(float(value)))
    else:
        return str(int(z))

def calculation_2():
    for x in text:
        s = x.split()
        for i in s:
            n2=0
            for j in i:
                if j.isdigit():
                    n2+=1
                    break
            if n2!=0:
                b=i
                for j in range (len(i)-1,-1,-1):
                    if i[j]=='(':
                        z=''
                        for k in range(j+1,len(i)):
                            if i[k]==')':
                                break
                            z+=i[k]
                        q = calculation_1(z)
                        i=i.replace('('+z+')',q)
                y=calculation_1(i)
                x=x.replace(b,y)
        print(x)
def max_consonants():
    a='бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩ'
    max_sum = -1
    for x in text:
        x1=x.split()
        for i in x1:
            sum = 0
            for j in i:
                if j in a:
                    sum +=1
            if sum > max_sum:
                max_sum = sum
                res = x
    print('Предложение, в котором слово с максимальным количеством согласных букв: ', res)

choice = None
text = ['С тех -5*(-(-1)) пор уже лет, может быть, двести эти ель и сосна вместе растут',
        'Их корни с малолетства сплелись, их стволы тянулись вверх рядом к свету, стараясь обогнать друг друга',
        'Деревья разных пород ужасно боролись между собою корнями за питание, сучьями за воздух и свет',
        'Поднимаясь все выше, толстея стволами, они впивались сухими сучьями в живые стволы и местами насквозь прокололи друг друга',
        'Злой ветер, устроив деревьям такую несчастную жизнь, прилетал сюда иногда покачать их',
        '']
n=len(text)
max_len = 0
for x in text:
    if len(x) > max_len:
        max_len = len(x)
        
while choice!='0':
    print(
        '''
1 - Выравнивание текста по левому краю.
2 - Выравнивание текста по правому краю.
3 - Выравнивание текста по ширине.
4 - Удаление заданного слова.
5 - Замена одного слова другим во всём тексте.
6 - Вычисление арифметического выражения.
7 - Индивидуальное задание: Найти предложение,
в котором слово с максимальным количеством согласных букв.
0 - Выход из меню
''')
    choice = input('Выбор: ')
    if choice == '0':
        print('Выход')
    elif choice == '1':
        left_side()
    elif choice == '2':
        right_side()
    elif choice == '3':
        width()
    elif choice == '4':
        delete_word()
    elif choice == '5':
        replace_word()
    elif choice == '6':
        calculation_2()
    elif choice == '7':
        max_consonants()