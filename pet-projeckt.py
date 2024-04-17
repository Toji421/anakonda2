#МАГАЗИН
print('Добый день! Вы сегодня хотите посетить где нибудь? ')
print("""Например:
1. Аквапарк
2. Кафе
3. Паб
4. Магазин""")
akva = (input('Выберите 1/2/3/4:   '))
if akva == "1":
    print('Вы выбрали Аквапарк')
    print("""Вот цены за вход""")
    print("0-3 бесплатно")
    print("3-7 200сом")
    print("7-12 400сом")
    print("12-18 600сом")
    akva2 = int(input("Сколько вам лет?  "))
    if 0<= akva2 <=3:
        print("Для вас вход бесплатно!")
    elif 3<= akva2 <=7:
        print("С вас 200сом")
    elif 7<= akva2 <=12:
        print("С вас 400сом")
    elif 12<= akva2 <=18:
        print("С вас 600сом")
    else:
        None
elif akva == "2":
    print("ВЫ ВЫБРАЛИ КАФЕ")
    print("1.CRAFT ЗАПАД")
    print("2.SIERRA Манас ")
    print("3.Чикен Стар")
    print("4.Белладжио Бэйкери&Вайн")
    print("5.Coffee Relax")
    print("6.Vanilla Sky")
    kafe = input("Какое кафе вы предпочитаете?  ")
    if kafe == "1":
        print("""
        Услуги: Есть терраса 
            · Барные игры и развлечения 
            · Здесь можно заказать еду в баре
                Часы работы: 
                четверг	15:00–03:00
                пятница	15:00–03:00
                суббота	15:00–03:00
                воскресенье 15:00–03:00
                понедельник 15:00–03:00
                вторник	15:00–03:00
                среда	15:00–03:00""")
        print("ул.Московская 208 / ул.Тимирязева Бишкек")
        print("Приятно провести время!")
    elif kafe == "2":
        print("""Часы работы: 
                четверг	07:30–23:00
                пятница	07:30–23:00
                суббота	07:30–23:00
                воскресенье	07:30–18:00
                понедельник	07:30–23:00
                вторник	07:30–23:00
                среда	07:30–23:00""")
        print("Адрес: 57, 1 просп. Манаса, Бишкек")
        print("Желаю хорошо провести время!")
    elif kafe == "3":
        print("""
            Услуги: Есть терраса 
            · Есть живая музыка    
            · Можно смотреть спортивные трансляции
            Часы работы: 
            пятница	11:00–22:30
            суббота	11:00–22:30
            воскресенье 11:00–22:30
            понедельник 11:00–22:30
            вторник	11:00–22:30
            среда	11:00–22:30
            четверг	11:00–22:30""")
        print('Адрес: Erkindik 36 Between Toktogula & Kievskaya, Бишкек')
    elif kafe == "4":
        print("""Часы работы: 
            пятница	08:00–00:00
            суббота	08:00–00:00
            воскресенье	08:00–00:00
            понедельник	08:00–00:00
            вторник 08:00–00:00
            среда   08:00–00:00
            четверг 08:00–00:00""")
        print("Адрес: 103 ул. Боконбаева, Бишкек")
        print("Приятного аппетита!")
    elif kafe == "5":
        print("""Услуги: Есть терраса 
                       · Вегетарианские блюда в меню 
                       · Есть детское меню
                       Часы работы: 
                    пятница	08:00–00:00
                    суббота	08:00–00:00
                    воскресенье	08:00–00:00
                    понедельник	08:00–00:00
                    вторник	08:00–00:00
                    среда	08:00–00:00
                    четверг	08:00–00:00""")
        print("Адрес: 140 ул. Токтогула, Бишкек")
        print("Желаю провести время хорошо!")
    elif kafe == "6":
        print("""Часы работы: 
                четверг	08:00–01:00
                пятница	08:00–01:00
                суббота	08:00–01:00
                воскресенье	08:00–00:00
                понедельник	08:00–01:00
                вторник	08:00–01:00
                среда	08:00–01:00""")
        print("Адрес: 147 ул. Московская, Бишкек")
        print("Желаю удачи вам что бы хорошо провести время!")
    else:
        None
elif akva == "3":
        print("Вам исполнилось 18?")
        akva3 = str(input(""))
        if akva3 == "нет":
            print("НЕСОВЕРШЕННОЛЕТНИМ ЗАПРЕШЕНО БУХАТЬ!!!")
        elif akva3 == "да":
            akva11 = str(input("""АЛДАБА НАН УРСУН ДЕЧИ!: """))
            if akva11 == "нан урсун":
                print("Добро пожаловать в пивной бар")
                print("""Что вы больше предпочитаете?
                    Например:
                    1.пиво
                    2.вино
                    3.ликёры
                    4.коктейли и безалкогольные напитки""")
                akva4 = str(input(""))
                if akva4 == "1":
                        print("""
                        1.Светлое пиво    
                        2.Тёмное пиво
                        3.Крафтовое пиво
                        4.Бельгия""")
                        akva5 = str(input('Какое пиво вы желаете?:  '))
                        if akva5 == "1":
                            print("1.Светлое пиво Spaten, Munchen, in can, 0.5 л")
                        print("Цена: 289сом")
                        print("""2.Светлое пиво "Dutch Windmill", in can, 0.5 л
                             Цена: 103сом""")
                        print("""3.Светлое пиво "Leffe" Blonde, 0.33 л
                             Цена: 289сом""")
                        print("""4.Светлое пиво "St. Pierre" Blanche, in can, 0.5 л
                             Цена: 110сом""")
                        print("""5.Светлое пиво "Prazacka" Svetle, in can, 0.5 л
                             Цена: 128сом""")
                        print("""6.Светлое пиво "Grotwerg" Alkoholfrei, in can, 0.5 л
                             Цена: 90сом""")
                        print("""7.Светлое пиво "Taiwan Beer" Gold Medal, in can, 0.5 л
                             Цена: 182сом""")
                        print("""8.Светлое пиво "Pilsner Urquell", in can, 0.5 л
                             Цена: 172сом""")
                        print("""9.Киликия" Светлое, 0.5 л
                             Цена: 169сом""")
                        print("""10.Светлое пиво Westmalle, "Trappist" Tripel, 0.33 л
                             Цена: 353сом""")
                        print("""11.Светлое пиво "Bakalar" Svetla Desitka, 0.5 л
                             Цена: 205сом""")
                        print("""12.Светлое пиво "Budweiser Budvar" Svetly Lezak, in can, 0.5 л
                             Цена: 215сом""")
                        print("""13.Светлое пиво "Kaiserberg" Weisse, in can, 0.5 л
                             Цена: 205сом""")
                        print("""14.Светлое пиво "Augustiner" Lagerbier Hell, 0.5 л
                             Цена: 396сом""")
                        print("""15.Liebenweiss" Hefe-Weissbier, mini keg, 5 л
                             Цена: 1930сом""")
                        akva6 = str(input("Какую пиву вы желаете?:  ")) 
                        if akva6 == "1":
                            print("Вы выбрали Светлое пиво Spaten, Munchen, in can, 0.5 л")   
                            akva7 = int(input("Свас 292 сома---> "))  
                            print("Приятно провести время!")
                        elif akva6 == "2":
                            print("Светлое пиво Dutch Windmill, in can, 0.5 л")
                            akv8 = int(input("Свас 103 сома--->  "))
                            print("Всего добрового")
                        elif akva6 == "3":
                            print("3.Светлое пиво Leffe Blonde, 0.33 л")
                            akva8 = int(input("Свас 289 сом--->  "))
                            print("Приятно провести время!")
                        elif akva6 == "4":
                            print(" Вы выбрали Светлое пиво St. Pierre Blanche, in can, 0.5 л")
                            akva9 = int(input("Свас 110 сом--->  "))
                            print("Всего добрового")
                        elif akva6 == "5":
                            print("Вы выбрали Светлое пиво Prazacka Svetle, in can, 0.5 л")
                            akva10 = int(input("128 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "6":
                            print("Вы выбрали Светлое пиво Grotwerg Alkoholfrei, in can, 0.5 л ")
                            akva10 = int(input("Свас 90 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "7":
                            print("Вы выбрали Светлое пиво Taiwan Beer Gold Medal, in can, 0.5 л ")
                            akva10 = int(input("Свас 182 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "8":
                            print("Вы выбрали Светлое пиво Pilsner Urquell, in can, 0.5 л ")
                            akva10 = int(input("Свас 172 сом---> "))
                            print("Всего добрового")
                        elif akva6 == "9":
                            print("Вы выбрали Киликия Светлое, 0.5 л ")
                            akva10 = int(input("Свас 179 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "10":
                            print("Вы выбрали Светлое пиво Westmalle, Trappist Tripel, 0.33 л")
                            akva10 = int(input("Свас 353 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "11":
                            print("Вы выбрали Светлое пиво Bakalar Svetla Desitka, 0.5 л ")
                            akva10 = int(input("Свас 205 сом---> "))
                            print("Всего добрового")
                        elif akva6 == "12":
                            print("Вы выбрали Светлое пиво Budweiser Budvar Svetly Lezak, in can, 0.5 л ")
                            akva10 = int(input("Свас 215 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "13":
                            print("Вы выбрали Светлое пиво Kaiserberg Weisse, in can, 0.5 л ")
                            akva10 = int(input("Свас 205 сом---> "))
                            print("Всего добрового")
                        elif akva6 == "14":
                            print("Вы выбрали Светлое пиво Augustiner Lagerbier Hell, 0.5 л")
                            akva10 = int(input("Свас 396 сом---> "))
                            print("Приятно провести время!")
                        elif akva6 == "15":
                            print("Вы выбрали Liebenweiss Hefe-Weissbier, mini keg, 5 л")
                            akva10 = int(input("Свас 1930 сом---> "))
                            print("Всего добрового")
                        else:
                            None
                elif akva4 == "2":
                        print("Вы выбрали вино!")
                        print("В нашем Пабе есть хороший ассортимент Вины, какую вы хотите?")
                        print("Красное вино/Белое вино/Розовое вино")
                        vino = str(input("1/2/3: "))
                        if vino == "1":
                            print("1.Каберне совиньон")
                            print("2.Мерло")
                            print("3.Пино нуар")
                            print("4.Мальбек")
                            print("5.Шираз")
                            print("6.Зинфандель")
                            vino2 = str(input("Какую предпочитаете? "))
                            if vino2 == '1':
                                vino3 = int(input("Свас 6900 сом---> "))
                                print("Перевод только на Мбанк! 0776421941")
                            elif vino2 == "2":
                                vino4 = int(input("Свас 1090 сом---> "))
                                print("Благодарю вас за покупку!")
                            elif vino2 == "3":
                                vino4 = int(input("Свас 1090 сом---> "))
                                print("Благодарю вас за покупку!")
                            elif vino2 == "4":
                                vino4 = int(input("Свас 1090 сом---> "))
                                print("Благодарю вас за покупку!")
                            elif vino2 == "5":
                                vino4 = int(input("Свас 1090 сом---> "))
                                print("Благодарю вас за покупку!")
                            elif vino2 == "6":
                                vino4 = int(input("Свас 1090 сом---> "))
                                print("Благодарю вас за покупку!")
                            else:
                                None
                        elif vino == "2":
                            print("Вы выбрали белое вино")
                            print("Javier Sanz — Вердехо")
                            print("Javier Sanz — Совиньон Блан")
                            print("Ама Вида")
                            print("Грюнер Вельтинер")
                            print("Шенен авек шене")
                            print("Пасаль де Есиле")
                            white_wine = str(input("Выберите Вино: "))
                            if white_wine == '1':
                                white_wine1 = int(input('Оплатите пожалуйста 1090сом '))
                                print('Блогардорю за покупку!')
                            elif white_wine == '2':
                                white_wine2 = int(input('Оплатите пожалуйста 1900сом'))
                                print('Блогардорю за покупку!')
                            elif white_wine == '3':
                                white_wine3 = int(input('Оплатите пожалуйста 1450сом'))
                                print('Блогардорю за покупку!')
                            elif white_wine == '4':
                                white_wine4 = int(input('Оплатите пожалуйста 1450сом'))
                                print('Блогардорю за покупку!')
                            elif white_wine == '5':
                                white_wine5 = int(input('Оплатите пожалуйста 2450сом'))
                                print('Блогардорю за покупку!')    
                            elif white_wine == '6':
                                white_wine6 = int(input('Оплатите пожалуйста 1990сом '))
                                print('Блогардорю за покупку!')   
                            else:
                                None  
                        elif vino == "3":
                            print("Вино Усадьба Дивноморское Терруар Вторая Линия Солист 0,75 л")
                            print("Розовое вино Chateau de Fesles La Chapelle Cabernet d'Anjou 0,75 л")
                            print("Вино Гай-Кодзор Розе 0,75 л")
                            print("Вино Усадьба Дивноморское Розе 2021 0,75 л")
                            print("Розовое вино Lustau Rose 0,75 л")
                            print("Розовое вино Lheraud Pineau des Charentes Collection Perle Rose 0,75 л")
                            pink_whine = str(input("Выберите одно из розовый Винов: "))
                            if pink_whine == '1':
                                pink_whine1 = int(input('Свас 988сом'))
                                print('Приятного отдыха')
                            elif pink_whine == '2':
                                pink_whine2 = int(input('Свас 1485сом'))  
                                print('Приятного отдыха')  
                            elif pink_whine == '3':
                                pink_whine2 = int(input('2890сом'))
                                print('Приятного отдыха')
                            elif pink_whine == '4':
                                pink_whine2 = int(input('1900сом'))
                                print('Приятного отдыха')
                            elif pink_whine == '5':
                                pink_whine2 = int(input('2890сом'))
                                print('Приятного отдыха')
                            elif pink_whine == '6':
                                pink_whine2 = int(input('3200сом'))
                                print('Приятного отдыха')    
                            else:
                                None
elif akva == "4":
    print("Вы решили прикупится: ")
    import random
food = str(input("Что вы желаете купить: "))
num = random.randrange(1,100)
print(f'Свас {num}сом')
food2 = str(input("Ещё что нибудь?: "))
if food2 == 'да':
    food3 = str(input(''))
    num2 = random.randint(1,100)
    result = num + num2
    print(f'Свас:{result}сом')
    print('БЛОГАДАРЮ ЗА ПОКУПКУ!')    
elif food2 == 'нет':
    print(f'Свас {num}сом')