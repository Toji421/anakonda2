import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGTH = HEIGHT // CELL_SIZE

#Цвета 
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (255, 0, 0)

#Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#Класс змейки
class snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGTH // 2)]
        self.direction = random.choise[UP , DOWN, LEFT, RIGHT]
        
    def move(self):
        new_head = (self.body[0][0], + self.direction[0], self.body[0][1], self.direction[1])
        
    def grow(self):
        self.body.append(self.body[-1])
        
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, WHITE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
#Главная функция игры
def main():
    
#Создание экрана
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("моя игра")
    
    # Создание Объекта
    clock = pygame.time.Clock()
    Snake = snake()
    food = (random.randint(0,  GRID_WIDTH -1), random.randint(0, GRID_HEIGTH -1))
 
#Установка цветов
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE = (255,0,0)

    #Позиция и размеры графического объекта
    player_size = 50
    playerx = WIDTH // 2 - player_size // 2
    playery  = HEIGHT - player_size

    #Скорость перемещение графического объекта
    player_speed = 5


# Основной игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            
                
        #Проверка нажатия клавишь
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.deraction != DOWN:
            snake.deraction != UP
        elif keys[pygame.K_DOWN] and snake.deraction != UP:
            snake.deraction != DOWN
        elif keys[pygame.K_RIGHT] and snake.deraction != LEFT:
            snake.deraction != RIGHT
        elif keys[pygame.K_LEFT] and snake.deraction != RIGHT:
            snake.deraction != LEFT
            playerx -= player_speed
        if keys[pygame.K_RIGHT]:
            playerx += player_speed
        

    # Закрашиваем экран черным цветом
        screen.fill((BLACK))
        snake.draw(screen)
        pygame.draw.rect(screen, BLUE, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
        #Обнавление экрана
        pygame.display.flip()    

        # Отображение изменений
        pygame.draw.rect(screen, BLUE,(playerx, playery, player_size, player_size))

# Выход из Pygame
pygame.quit()
sys.exit()

if __name__ == "__name__":
    main(  )