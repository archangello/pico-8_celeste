import bhaskara
import pygame

pygame.init()
display = pygame.display.set_mode((600, 600))


is_running  = True
def rodando():
    global is_running
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_running = False
            pygame.quit()
    return is_running
w = 20
h = 20
y = display.height - h - 10
x = display.width / 2 - w / 2
def draw_square():
    pygame.draw.rect(display, (255, 255, 255), (x, y, w, h))


moviment = bhaskara.QuadraticMovement(duration=1.0)


clock = pygame.Clock()
while rodando():
    dt = clock.tick(60) / 1000

    if not moviment.is_animating:
        y = display.height - h - 10
        moviment.start()

    y -= moviment.update(delta_time=dt) or 0
    
    display.fill((0, 0, 0))
    draw_square()
    
    pygame.display.flip()
    

