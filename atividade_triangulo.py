import glfw
from OpenGL.GL import *
import numpy as np

# Função que cria a matriz de translação


def create_translation_matrix(tx, ty):
    return np.array([
        [1.0, 0.0, 0.0, tx],
        [0.0, 1.0, 0.0, ty],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

# Função que cria a matriz de escala


def create_scale_matrix(sx, sy):
    return np.array([
        [sx, 0.0, 0.0, 0.0],
        [0.0, sy, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)


# Inicializa janela
glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
window = glfw.create_window(
    800, 600, "Translação e Escala com Matriz", None, None)
glfw.make_context_current(window)

# Posições e escala
x_pos, y_pos = 0.0, 0.0
scale = 1.0
speed = 0.001
scale_speed = 0.001  # velocidade de escala

while not glfw.window_should_close(window):
    glfw.poll_events()

    # Teclas de movimento
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        x_pos -= speed

    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        x_pos += speed

    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        y_pos += speed

    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        y_pos -= speed

    # Tecla de escala - S aumenta e  A diminui
    if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
        scale += scale_speed

    if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        scale -= scale_speed
        if scale < 0.1:
            scale = 0.1

    # Limpa tela
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Cria matrizes de transformação
    translation_matrix = create_translation_matrix(x_pos, y_pos)
    scale_matrix = create_scale_matrix(scale, scale)

    # Combina escala e depois translação (ordem importa!)
    transform_matrix = np.matmul(translation_matrix, scale_matrix)

    glLoadMatrixf(transform_matrix.T)  # OpenGL usa matriz coluna principal

    # Desenha triângulo
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 1, 0)
    glVertex2f(0.5, -0.5)
    glColor3f(0, 0, 1)
    glVertex2f(0.0, 0.5)
    glEnd()

    glfw.swap_buffers(window)

glfw.terminate()
