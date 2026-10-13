#define cube_x       40
#define cube_y       80
#define cube_size    50
#define cube_color_r 101
#define cube_color_g 154
#define cube_color_b 210

void draw_cube(void *buffer, int pitch, int psize) {
    unsigned char *pixels = (unsigned char*)buffer;

    // pitch: quantidade de bytes ocupados por uma linha inteira da imagem,
    // incluindo possíveis bytes de preenchimento (padding).
    //
    // psize: quantidade de bytes por pixel. Por exemplo, 3 para RGB
    // ou 4 para formatos de 32 bits, como RGBA.
    //
    // Para acessar um pixel (x, y), calculamos:
    //   y * pitch   -> deslocamento até o início da linha y;
    //   x * psize   -> deslocamento até o pixel x dentro dessa linha.
    //
    // Somamos os dois deslocamentos para obter o endereço do pixel.
    // O índice final acessa um canal específico dentro desse pixel.
    
    /*
     * FORMATO DOS PIXELS E ORDEM DOS CANAIS
     *
     * O buffer armazena bytes, não cores com nomes como vermelho ou azul.
     * A ordem em que os canais aparecem na memória depende do formato
     * de pixel utilizado pela superfície gráfica.
     *
     * RGB: [R][G][B]
     * BGR: [B][G][R]
     *
     * Neste código, assumimos que o buffer utiliza BGR:
     *   +0 -> Azul
     *   +1 -> Verde
     *   +2 -> Vermelho
     *
     * Por isso, os valores RGB são escritos nos deslocamentos inversos:
     *   pixels[pixel_index + 2] = cube_color_r;
     *   pixels[pixel_index + 1] = cube_color_g;
     *   pixels[pixel_index + 0] = cube_color_b;
     *
     * A ordem dos canais não é universal: depende do formato de pixel
     * utilizado pela superfície e pela biblioteca gráfica.
     *
     * Isso também não deve ser confundido com endianess, que determina
     * a ordem dos bytes de valores multibyte na memória.
     *
     * Para verificar o formato de uma pygame.Surface, consulte:
     *   surface.get_bytesize() -> bytes por pixel;
     *   surface.get_pitch()    -> bytes por linha;
     *   surface.get_masks()    -> máscaras dos canais de cor;
     *   surface.get_shifts()   -> deslocamentos dos canais.
     *
     * Atenção: esses métodos descrevem a superfície consultada.
     * Confirme que ela corresponde ao buffer que está sendo modificado.
     */
    for (int i=cube_y; i < cube_y+cube_size; i++) {
        for (int j=cube_x; j < cube_x+cube_size; j++) {
            pixels[(i*pitch + j*psize) + 2] = cube_color_r;
            pixels[(i*pitch + j*psize) + 1] = cube_color_g;
            pixels[(i*pitch + j*psize) + 0] = cube_color_b;
        }
    }
}
// Você pode compilar com:
// gcc -shared -fPIC test.c -o test.o

// + Python:
// gcc -shared -fPIC test.c -o test.o | python teste_c.py
