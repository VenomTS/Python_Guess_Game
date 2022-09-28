from Board import Board
import pygame

pygame.init()

pygame.display.set_caption("Guess Game")

WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def drawBorders(surface, rows):
    for i in range(0, WIDTH, WIDTH // rows):
        pygame.draw.line(surface, BLACK, (i, 0), (i, HEIGHT), 1)
    for i in range(0, HEIGHT, HEIGHT // rows):
        pygame.draw.line(surface, BLACK, (0, i), (WIDTH, i), 1)

def drawSelectedSpot(surface, board):
    for spot in board.hidden:
        w, h = WIDTH // board.n, HEIGHT // board.n
        startPosX, startPosY = spot.row * w, spot.col * h
        pygame.draw.rect(surface, RED, pygame.Rect(startPosX, startPosY, w, h))
    for spot in board.selected:
        w, h = WIDTH // board.n, HEIGHT // board.n
        startPosX, startPosY = spot.row * w, spot.col * h
        pygame.draw.rect(surface, GREEN, pygame.Rect(startPosX, startPosY, w, h))

def manySelected(board):
    n = len(board.selected)
    if n == board.n:
        return False
    return True

def writeText(font, surface, board):
    for spot in board.selected:
        text = font.render(spot.letter, True, BLACK)
        textRect = text.get_rect()
        w, h = WIDTH // board.n, HEIGHT // board.n
        centerX, centerY = (spot.row * w) + w // 2, (spot.col * h) + h // 2
        textRect.center = (centerX, centerY)
        surface.blit(text, textRect)


def main():
    myBoard = Board("TestGame")
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    surface.fill(WHITE)
    font = pygame.font.SysFont('ariel.ttf', WIDTH // myBoard.n)
    while manySelected(myBoard):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                wDiv = WIDTH // myBoard.n
                hDiv = HEIGHT // myBoard.n
                x //= wDiv
                y //= hDiv
                myBoard.selectSpot(x, y)
                drawSelectedSpot(surface, myBoard)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit("Game Forcefully Ended")
        drawBorders(surface, myBoard.n)
        pygame.display.update()
    writeText(font, surface, myBoard)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit("Game Finished")

main()
