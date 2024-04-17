day = int(input('Выберите день: '))
month = int(input('Выберите месяц: '))

#Задиак Овен
if (day>=21 and day<=31 and month==3) or (month==4 and day>=1 and day <=19):
    print('Вы Овен')

#Задиак Телец
elif (day>=21 and day<=30 and month==4) or (month==5 and day>=1 and day <=20):
    print('Ты телец')
    
# Зодиак Близнецы
elif (day>=21 and day<=31 and month==5) or (month==6 and day>=1 and day <=21):
    print('Вы Близнецы')

#Зодиак Рак
elif (day>=22 and day<=30 and month==6) or (month==7 and day>=1 and day<=22):
    print('Вы Рак')

# Зодиак Лев
elif (day>=23 and day<=31 and month==7) or (month==8 and day>=1 and day<=23):
    print('Вы Лев')

# Зодиак Дева
elif (day>=24 and day<=31 and month==8) or (month==9 and day>=1 and day<=23):
    print('Вы Дева')

#Зодиак Весы
elif (day>=24 and day<=30 and month==9) or (month==10 and day>=1 and day<=23):
    print('ВЫ Весы')
    
#Зодиак Скорпион
elif (day>=24  and day<=31  and month==10) or (month==11 and day>=1 and day<=22):
    print('Вы Скорпион')

#Зодиак Стрелец
elif(day<=23 and day>=30 and month==11) or (month==12 and day>=1 and day<=21):
    print('Вы Стрелец')

# Зодиак Козерог
elif(day>=22 and day<=31 and month==12) or (month==1 and day>=1 and day<=20):
    print('Вы Козерог')

# Зодиак Водолей
elif(day>=21 and day<=31 and month==1) or (month==2 and day>=1 and day<=20):
    print('Вы Водолей')

# Зодиак Рыба
elif(day>=21 and day<=28 and month==2) or (month==3 and day>=1 and day<=20):
    print('Вы Рыба')

elif(day>=29 and day<=31 and month==2):
    print('Inncorret date!')
    if month == '0':
        print('Inncorret month')
    elif day == '0':
        print('Inncorret day')

