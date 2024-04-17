import pygame


pygame.init()

screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption('Игры маза фака')
icon = pygame.image.load('лвл1.css\Stroka\images\images.jpeg')
pygame.display.set_icon(icon)


# square = pygame.Surface((100,10))
# square.fill('red')

myfont = pygame.font.Font(None, 40)
# text = myfont.render('KAYLAS', False, 'red')


player = pygame.image.load('лвл1.css\Stroka\images\images.jpeg')


# line_start = (150, 150)
# line_end = (250, 150)
# line_color = (255, 110, 0)


dis = True
while True:
    
    screen.fill((199, 207, 89))
    
    # screen.blit(text, (250, 180))
    screen.blit(player, (0, 0))
    # pygame.draw.line(screen, line_color, line_start, line_end, 5)
    # pygame.draw.circle(screen, 'Red', (250, 150), 100)
    # pygame.draw.circle(screen, 'Black', (210, 140), 10)
    # pygame.draw.circle(screen, 'Black', (280, 140), 10)
    # screen.blit(square, (200, 190))
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()