
import pygame
clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((650, 415))

# Название игры
pygame.display.set_caption('Игра ииуу')

# загрузка заднего фона
bg = pygame.image.load('game/images/bg.png')

# Загрузка машины изображения
car_evil = pygame.image.load('game/images/car_1.png')



# Изображения аватара
walk_left = [
    pygame.image.load('game/images/left_1.png.png'),
    pygame.image.load('game/images/left_2.png.png'),
    pygame.image.load('game/images/left_3.png.png'),
    pygame.image.load('game/images/left_2.png.png'),
]

walk_right = [
    pygame.image.load('game/images/right_1.png.png'),
    pygame.image.load('game/images/right_2.png.png'),
    pygame.image.load('game/images/right_3.png.png'),
    pygame.image.load('game/images/right_2.png.png'),
]

car_list = []

bullet = pygame.image.load('game/images/image-586005.png')
bullets = []


player_x = 350
player_y = 340
player_jump = False
jump_count = 10
player_speed = 8
player_anim_count = 0

bg_x = 0

car_x = 655


# Музыка 
sound = pygame.mixer.Sound('game/sound/song.mp3')

# Музыка Game Over
game_over_sound = pygame.mixer.Sound('game/sound/GameOver.mp3')
sound.play()

# задний фон после смерти
game_over_bg = pygame.image.load('game/images/icon.jpg')




# Новые размеры для аватара (меньшие значения)
new_width = 30  # Новая ширина
new_height = 30  # Новая высота

car_timer = pygame.USEREVENT + 1
pygame.time.set_timer(car_timer, 1000)


logica = False

# Логика рестарта и проигрыша
label = pygame.font.Font(None, 40)
lose_label = label.render('Game Over', logica, (210, 196, 199))
restart_label = label.render('RESTART' , logica, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(200, 200))


 


bullets_left = 15
game_play = True
running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 650, 0))
        
    # Пуля
    # screen.blit(bullet,(0,0))
    
    
    if game_play:
        
    
        player_rect = walk_left[0].get_rect(topleft = (player_x, player_y)) 
        
        if car_list:
            for (el,i)in enumerate (car_list):
                screen.blit(car_evil, i)
                i.x -= 10
                
                if i.x < - 10:
                    car_list.pop(el)
                
                if player_rect.colliderect(i):
                    game_play = False
                    sound.stop()                    
                    game_over_sound.play()
            
                    
        
        # Движении логики
        keys = pygame.key.get_pressed()
        # Анимация игрока
        if keys[pygame.K_LEFT] and player_x > 1:
            # Отображение анимации движения влево
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else: 
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        if keys[pygame.K_LEFT] and player_x > 1:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 630:
            player_x += player_speed

        

        # Прыжок
        if not player_jump:
            if keys[pygame.K_SPACE]:
                player_jump = True
                jump_count = 10 # Сброс счетчик прыжка
        
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                player_jump = False
            
    
    
            
    # Цикл обновление индекса анимации
    # player_anim_count  %=  len(walk_left)

        bg_x -= 2
        if bg_x == -650:
            bg_x = 0
            
        if bullets:
            for (el, i) in enumerate(bullets):
                screen.blit(bullet, (i.x ,i.y))
                i.x += 4 
                
                if i.x >630:
                    bullets.pop(el) 
                
                if car_list:
                    for (index, car_el) in enumerate(car_list):
                        if i.colliderect(car_el):
                            car_list.pop(index)
                            bullets.pop(el)
    
    
        
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game_play =  True
            player_x = 70
            car_list.clear()
            bullets.clear()
            bullets_left = 15
        else:
            screen.blit(lose_label, (180, 100))
            screen.blit(game_over_bg,(0,0))
            screen.blit(restart_label, restart_label_rect) 
        
           
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == car_timer:
            car_list.append(car_evil.get_rect(topleft=(630, 300 )))

        # Рисунка патрона
        if game_play and event.type == pygame.KEYUP and event.key == pygame.K_b \
            and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft = (player_x + 30, player_y + 10)))
            bullets_left -= 1
    
    
    clock.tick(40)
