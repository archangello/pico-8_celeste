from c_caller import Caller
import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
call_c = Caller(display, 'test.o')

rodando = True
def is_running():
    global rodando
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False
            pygame.quit()
    return rodando

clock = pygame.Clock()
while is_running():
    clock.tick(30)
    call_c()
    pygame.display.flip()