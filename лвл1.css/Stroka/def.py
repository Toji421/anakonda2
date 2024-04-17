# # # Калькулятор с функции def
# # def calculator():
# #     print('Выберите функцию')
# #     print('1)+')
# #     print('2)-')
# #     print('3)/')
# #     print('4)*')
# #     num = int(input(''))
# #     number_1 = int(input())
# #     number_2 = int(input())
# #     if num == 1:
# #         result_1 = number_1 + number_2
# #         print(result_1)
# #     elif num == 2:
# #         result_2 = number_1 - number_2
# #         print(result_2)
# #     elif num == 3:
# #         result_3 = number_1 / number_2
# #         print(result_3)
# #     elif num == 4:       
# #         result_4 = number_1 * number_2
# #         print(result_4)
            
# # print(calculator())



# # Угадай цифру
# # import random

# # def number():
# #     jun = random.randint(1,2)
# #     print('Добро пожаловать в игру "Отгадай число!"')   
# #     life = 0
    
# #     while True:
# #         number = int(input('Ваше предположениие: '))
# #         life += 1
# #         if jun == number:
# #             print(f'Вы угадали число {jun} с {life} попытки')
# #             break
# #         elif jun < number:
# #             print('Ваше число меньше')
# #         elif jun > number:
# #             print('Ваше число больше')


# # number()
        
    

# # Угадай слово

# # import random


# # def sentens():
# #     print('Добро пожаловать в игры угадай слово!')
# #     print('Эти слова относятся к Школьным предметам')
# #     print('ручка', 'карандаш',' тетрадь','книга','учительница','парта','доска','ЧМО')
# #     text_1 = ('ручка', 'карандаш',' тетрадь','книга','учительница','парта','доска','ЧМО')
# #     text = random.choice(text_1)
# #     shans = 0
    
# #     while True:
# #         secret = str(input(""))
# #         shans +=1
# #         if text == secret:
# #             print(f'Ты отгадал за {shans} попытки, молодец!')
# #             break
# #         else:
# #             print('Попробуй ещё раз')
            
# # sentens()


# # Угадай слово по буквам
# # import random


# # def play_game(word):
# #     letter = ['_']*len(word)
# #     attems = 0
    
    
# #     print('Добро пожаловать в игру "Угадай слово"!')
# #     print('алма', 'алмурут', 'банан', 'жузум', 'шабдалы', 'орук', 'апельсин',)
# #     while True:
# #         print('\nУгаданные буквы:' + ''.join(letter))
# #         guess = input('Введите букву: ').lower()
        
# #         if len(guess) !=1 or not guess.isalpha:
# #             print('Введите только одну букву')
# #             continue
# #         if guess in letter:
# #             print('Вы уже угадали эту букву.')
# #             continue
# #         if guess in word:
# #             print('Поздравляю вы угадали слово! ')
# #             for i in range(len(word)):
# #                 if word[i] == guess:
# #                     letter[i] = guess
# #         else:
# #             print('К сожелению такой буквы нету здесь.')
# #             attems +=1
# #         if '_' not in letter:
# #             print('Поздравляю! Вы угадали слово.')
# #             return False
# # def main():
# #     words = ['алма', 'алмурут', 'банан', 'жузум', 'шабдалы', 'орук', 'апельсин', ]
# #     word_guess_one_word = random.choice(words)
# #     play_game(word_guess_one_word)
# # if __name__ == '__main__':
# #     main()


# # def num():
# #     a = int(input('Введите число: '))
# #     b = int(input('Введите 2 число: '))
# #     c = int(input('Введите 3 число: '))
# #     d = a + b + c
# #     print(d)
                
# # num()


# # def number_on():
# #     number_1 = int(input('Введите число: '))
# #     number_2 = int(input('Введите 2 число: '))
# #     if number_1 > number_2:
# #         print(f'{number_1} больше чем {number_2}')
# #     elif number_1 < number_2:
# #         print(f'{number_1} меньше чем {number_2}')
        
# # number_on()

# # def zoo():
# #     print('Добро пожаловать в Зоопарк!')
# #     age = int(input('Сколько вашему сыну? '))
# #     if 0< age <3:
# #         print('Вход бесплатно!')
# #     elif 3<= age <5:
# #         print('С вас 100 сом')
# #     elif 5<= age <8:
# #         print('Свас 200 сом')
# #     elif 8<= age <12:
# #         print('С вас 300 сом')
# #     elif 12<= age <18:
# #         print('С вас 500 сом')
# #     else:
# #         print('Вход только младше 18')
# # zoo()



# # import random
# # import time


# # def number():
# #     print('Подбросил монетку...')
# #     a = random.randint(1,2)
# #     if a == 1:
# #         time.sleep(2)
# #         print(' выпал Орёл!')
# #     elif a == 2:
# #         time.sleep(2)
# #         print('выпал Решка!')
# # number()


    

# # import random
# # import time

# # def game():
    
# #     print('Камень, ножница, бумага')
# #     time.sleep(0.5)
# #     txt = ['камень', 'ножница', 'бумага' ]
# #     player_choice = input('Твой выбор: ')
# #     komputer_choice = random.choice(txt)
    
    
# #     print(f'компютер выбрал  {komputer_choice}')
# #     print(f'Вы выбрали  {player_choice}')
    
# #     if player_choice not in txt:
# #         print('Неверный выбор, Попробуй ещё раз')
# #         return 
    
# #     elif player_choice == komputer_choice:
# #         time.sleep(3)
# #         print('Ничья!')
        
# #     elif(player_choice == 'камень' and komputer_choice == 'ножница') or\
# #         (player_choice == 'ножница' and komputer_choice == 'бумага') or\
# #         (player_choice == 'бумага' and komputer_choice == 'камень'):
# #         time.sleep(3)
# #         print('Вы победили!')
        
# #     else:
# #         time.sleep(3)
# #         print(f'{komputer_choice} победил!')
        
# # game()



