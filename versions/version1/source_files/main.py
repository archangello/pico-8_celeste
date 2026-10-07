import pygame
from pygame.math import lerp as larp

pygame.init()

display = pygame.display.set_mode((800, 600))

rodando = True

player_size: int    = 40
player_x: float     = display.width / 2 - player_size / 2
player_y: float     = display.height / 2 - player_size / 2
jump_force: float   = 80
jump_duration: float = 0.1
player_speed: float = 10
player_hyper_speed: float = 25
direction_x = 0
direction_y = 0

gravity = 6

floor_h = 40
floor_y = display.height - floor_h

clock = pygame.Clock()

def draw_floor():
    pygame.draw.rect(display, (0, 255, 0), (0, floor_y, display.width, floor_h))

def draw_player():
        pygame.draw.rect(display, (255, 255, 255), (player_x, player_y, player_size, player_size))
        match direction_y:
            case -1:
                pygame.draw.rect(display, (255, 0, 0), (player_x, player_y, player_size, player_size / 4))
            case 1:
                pygame.draw.rect(display, (255, 0, 0), (player_x, player_y + player_size - player_size / 4, player_size, player_size / 4))
            
            case _: pass
        
        match direction_x:
            case -1:
                pygame.draw.rect(display, (255, 0, 0), (player_x, player_y, player_size / 4, player_size))
            case 1:
                pygame.draw.rect(display, (255, 0, 0), (player_x + player_size - player_size / 4, player_y, player_size / 4, player_size))
            
            case _: pass
      

larp_atual = 0
y1 = player_y
y2 = player_y
jumping = False

while rodando:
    direction_x = 0
    direction_y = 0
    delta = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            quit(0)

    old_player_y = player_y

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        direction_x = -1
    if teclas[pygame.K_d]:
        direction_x = 1
    if teclas[pygame.K_w]:
        direction_y = -1
    if teclas[pygame.K_s]:
        direction_y = 1
        player_y += player_speed

    if teclas[pygame.K_h] and player_y >= floor_y - player_size:
        jumping = True
        y1 = player_y
        y2 = player_y - jump_force
        larp_atual = 0
    
    if teclas[pygame.K_SPACE]: # DASH!
        player_x += player_hyper_speed * direction_x
        player_y += player_hyper_speed * direction_y
    
    if player_y < floor_y - player_size:
        player_y += gravity
    elif player_y > floor_y - player_size:
        player_y = floor_y - player_size

    if jumping:
        larp_atual = larp_atual + delta / jump_duration
        player_y = larp(y1, y2, larp_atual)

        if larp_atual >= 1.0:
            jumping = False

    player_x += player_speed * direction_x

    display.fill((0, 0, 3))
    draw_floor()
    draw_player()

    pygame.display.flip()

# def algum_codigo():
#     with open('filename', 'rb') as file: # obs: Dá erro se o arquivo não existir
#         conteudo: bytes = file.read() # type: ignore
#     pixel_atual: int = 0
#     # esse vai ser o numero que vai guardar a chave correspondente ao nosso pixel
    
#     posit_byte      : int = 0
#     posit_bits      : int = 0
#     pixel_sep       : int = 1
#     pixel_sep_old   : int = 0
#     channel_red   : int = 0
#     channel_green : list = 0
#     channel_blue  : list = 0
#     channel       : int = 0
#     for posit_byte in range(pixel_sep_old * 8, len(file.read), pixel_sep * 8):
        
#         byte_cur = [int(bit) for bit in range(pixel_sep_old * 8, pixel_sep * 8)]
#         match channel:
#             case 0:
#                 channel_red   = byte_cur
#                 channel += 1
#             case 1:
#                 channel_green = byte_cur
#                 channel += 1
#             case 2:
#                 channel_blue  = byte_cur
#                 channel = 0
#                 # // lista dos bits que eu selecionei
#                 # // basicamente, eu to selecionando partes de 8 bits da imagem
#                 # // e ai cada uma dessas partes vai corresponder a um channel
#                 # // 0 nesse match e o vermelho, 1 o verde, 2 o azul
#                 # // quando chegar em 2 volta ao 0 e eu continuo o for para comtinuar para o proximo pixel
        
#     pixel_channel: list = [channel_red, channel_green, channel_blue]
