#define cube_x       40
#define cube_y       80
#define cube_size    50
#define cube_color_r 101
#define cube_color_g 154
#define cube_color_b 210

void draw_cube(void *buffer, int pitch, int psize) {
    unsigned char *pixels = (unsigned char*)buffer;

    // calculo: (yw + xp) + canal
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