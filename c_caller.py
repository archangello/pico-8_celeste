import pygame
import ctypes

class Caller:
    def __init__(self, pygame_surface: pygame.Surface, lib_name: str):
        self.surface = pygame_surface
        view = self.surface.get_view("0") # Extrai o buffer como uma Array C
        ptr = ctypes.addressof(ctypes.c_ubyte.from_buffer(view)) # Converte a array para bytes e obtem o ponteiro
        self.c_buffer_ptr = ctypes.c_void_p(ptr) # converte o ponteiro para algo que o C entende

        self.cdll = ctypes.CDLL(lib_name)
        self.c_func = self.cdll.main # Importa a função `main` por padrão

        self.c_func.argtypes = [ctypes.c_void_p, ctypes.c_int] # tipo de cada parâmetro
        self.c_func.restype = None # Tipo de resposta (void)
    def __call__(self):
        self.c_func(
            self.c_buffer_ptr,
            ctypes.c_int(self.surface.get_pitch()),
            ctypes.c_int(self.surface.get_bytesize())
        )
