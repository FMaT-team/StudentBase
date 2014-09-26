# StudentBase v0.1
# Created by FMaT-team

numbers = [

    {'number' : '5353535', 'surname' : 'Гашков', 'adress' : 'Биржевая площадь'},
    {'number' : '7582398', 'surname' : 'Гончар', 'adress' : 'Проспект Героев'},
    {'number' : '5519158', 'surname' : 'Лабчук', 'adress' : 'Детская улица'},
    {'number' : '3618224', 'surname' : 'Генько', 'adress' : 'Гладкий остров'},
    {'number' : '7542282', 'surname' : 'Цветков', 'adress' : 'Улица Дегтярева'},
    {'number' : '1154862', 'surname' : 'Бурков', 'adress' : 'Улица Танкистов'},
    {'number' : '2410250', 'surname' : 'Кравчук', 'adress' : 'Улица Тарасова'},
    {'number' : '8205348', 'surname' : 'Плешков', 'adress' : 'Улица Уточкина'},
    {'number' : '7364528', 'surname' : 'Ушаков', 'adress' : 'Улица Чехова'},
    {'number' : '4125266', 'surname' : 'Жукова', 'adress' : 'Кронверский проспект'}

        ]

while True:

    x = 0
    try:
        for i in numbers:
            x += 1
    except:
        x += 0

    """
    from tkinter import *
    root = Tk()

    ShowAll = Button(root)
    ShowAll['text'] = 'Просмотреть весь справочник'

    y = 0
    while y < x:
        
        def printer(event):
            print(numbers[y-1]['number'], numbers[y-1]['surname'], numbers[y-1]['adress'])
        ShowAll.bind('<Button-1>', printer)
       
        ShowAll.pack()
        
        root.mainloop()
        y = y + 1
        print(y)
    """  

    a = input()

    if a == '1':
        y = 0
        while y < x:
            print(numbers[y]['number'], ',', numbers[y]['surname'], ',', numbers[y]['adress'])
            y += 1
            
    if a == '2':
        surname = input("Введите фамилию: ")
        adress = input("Введите адрес: ")
        number = input("Введите телефон: ")
        numbers.append({'number':number, 'surname' : surname, 'adress' : adress})

    if a == '3':
        number = input("Введите искомый номер: ")
        for x in numbers:
            if number in x['number']: print(x['number'], ',', x['surname'], ',', x['adress'])

    if a == '4':
        surname = input("Введите искомую фамилию: ")
        for x in numbers:
            if surname in x['surname']: print(x['number'], ',', x['surname'], ',', x['adress'])

    if a == '5':
        adress = input("Введите искомый адрес: ")
        for x in numbers:
            if adress in x['adress']: print(x['number'], ',', x['surname'], ',', x['adress'])

    if a == '6':
        break
