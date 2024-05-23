import pygame
import os

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

x_image_path = os.path.join('D:\\', 'PythonProjects', 'venv', 'X.png')
o_image_path = os.path.join('D:\\', 'PythonProjects', 'venv', 'O.png')

img_x = pygame.image.load(x_image_path)
img_o = pygame.image.load(o_image_path)

img_x = pygame.transform.scale(img_x, (200, 200))
img_o = pygame.transform.scale(img_o, (200, 200))

player = 1
game_over = False
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(win, BLACK, (x * WIDTH // 3, 0), (x * WIDTH // 3, HEIGHT), 5)
        pygame.draw.line(win, BLACK, (0, x * HEIGHT // 3), (WIDTH, x * HEIGHT // 3), 5)

# Desenha  X ou O no quadrado selecionado
def draw_player(row, col):
    if matrix[row][col] == 1:
        win.blit(img_x, (col * WIDTH // 3 + (WIDTH // 6 - 100), row * HEIGHT // 3 + (HEIGHT // 6 - 100)))
    elif matrix[row][col] == 2:
        win.blit(img_o, (col * WIDTH // 3 + (WIDTH // 6 - 100), row * HEIGHT // 3 + (HEIGHT // 6 - 100)))

# Verifica o estado do jogo
def check_game_over():
    # Verifica linhas e colunas
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
            return matrix[i][0]  # Retorna o número do jogador que venceu
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
            return matrix[0][i]  # Retorna o número do jogador que venceu
    # Verifica diagonais
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        return matrix[0][0]  # Retorna o número do jogador que venceu
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
        return matrix[0][2]  # Retorna o número do jogador que venceu
    # Verifica empate
    if all(matrix[i][j] != 0 for i in range(3) for j in range(3)):
        return 0  # Retorna 0 para indicar empate
    return None  # Retorna None se o jogo ainda está rodando

# Loop principal do jogo
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // (HEIGHT // 3)
            col = pos[0] // (WIDTH // 3)
            if matrix[row][col] == 0:
                matrix[row][col] = player
                player = 1 if player == 2 else 2

    # Limpa a tela com fundo branco
    win.fill(WHITE)

    # Desenha a grade do jogo
    draw_grid()

    # Desenha X ou O nos quadrados selecionados
    for row in range(3):
        for col in range(3):
            if matrix[row][col] != 0:
                draw_player(row, col)

    # Exibe de quem é a vez
    font = pygame.font.Font(None, 36)
    text = font.render("Vez do jogador X" if player == 1 else "Vez do jogador O", True, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

    # Verifica se o jogo acabou
    winner = check_game_over()
    if winner is not None:
        if winner == 1:
            game_over_text = font.render("Jogador X venceu!", True, BLACK)
            print("Jogador X venceu!")
        elif winner == 2:
            game_over_text = font.render("Jogador O venceu!", True, BLACK)
            print("Jogador O venceu!")
        else:
            game_over_text = font.render("Empate!", True, BLACK)
            print("Empate!")
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 30))
        game_over = True  # Define game_over como True para sair do loop

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
pygame.quit()
