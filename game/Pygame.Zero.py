import pgzrun


backround = ('game\\images\bg.png')
def draw():
    screen.clear()
    screen.blit(backround,(0,0))
    screen.draw.text("Hello, Pygame Zero!", (100, 100), color="white")

def update():
    pass

pgzrun.go()