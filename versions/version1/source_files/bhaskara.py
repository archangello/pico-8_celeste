class QuadraticMovement:
    def __init__(self, duration: float):
        self.duration = max(duration, 0)
        self.a = -5
        self.b = self.duration * 5
        self.c = 0
        self.current_x = 0
        self.is_animating = False

    def start(self):
        self.current_x = 0
        self.is_animating = True

    def update(self, delta_time: float) -> float | None:
        """Atualiza a posição da trajetória quadrática ao longo do tempo.

        Calcula o valor de y para a curva definida pelos coeficientes a, b e c
        utilizando o deslocamento atual em x, incrementando o tempo da animação
        até atingir o limite configurado. Quando o movimento termina, a animação
        é interrompida.

        Args:
            delta_time (float): Tempo em segundos desde o último frame.

        Returns:
            float: Valor de y calculado para a posição atual da animação.
            None: Quando a animação não está acontecendo
        """
        if not self.is_animating:
            return None

        y = (self.a * self.current_x**2) + (self.b * self.current_x) + self.c
        self.current_x += delta_time

        if self.current_x >= self.duration:
            self.is_animating = False

        return y