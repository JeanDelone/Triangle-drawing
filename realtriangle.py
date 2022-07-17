import pygame
from pygame import gfxdraw
import random
from sys import exit

pygame.init()

BLUE = (109,207,246)
RED = (255,0,0)
WHITE = (255,255,255)

WIDTH = 1920
HEIGHT = 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
fps = 5
iterations = 1

kwadratXD = [(20,20),(1020,1020),(20,1020),(1020,20)]
kordy_kwadratu = (520,520)

left_triangle = [(495,150),(45,HEIGHT-150), ((WIDTH/2) -45, HEIGHT -150)]
right_triangle = [(495 + (WIDTH/2),150),(WIDTH - 45,HEIGHT-150), ((WIDTH/2) + 45, HEIGHT -150)]
current_coordinates = (495,540)

iterations = 0
font = pygame.font.Font(None, 50)
def subtitles():
    subtitles_surf = font.render(f"Iterations: {iterations}", False, (255,255,255))
    pygame.draw.rect(WIN, (0,0,0), ((WIDTH / 2) -200, 100, 600,50))
    WIN.blit(subtitles_surf, ((WIDTH / 2) - 200, 100))


def draw_left_half():
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(0,0,WIDTH/2,HEIGHT))
    for point in left_triangle:
        gfxdraw.pixel(WIN, int(point[0]), int(point[1]), BLUE)

def draw_right_half():
    for point in right_triangle:
        gfxdraw.pixel(WIN, int(point[0]), int(point[1]), WHITE)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # If pressed key is ESC quit program
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    random_point = random.choice(left_triangle)
    draw_left_half()
    draw_right_half()
    pygame.draw.line(WIN, BLUE, current_coordinates, (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))) 
    current_coordinates = (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))
    gfxdraw.pixel(WIN, int(current_coordinates[0] + (WIDTH / 2)), current_coordinates[1], WHITE)

    random_point = random.choice(left_triangle)
    # for point in left_triangle:
    #     gfxdraw.pixel(WIN, int(point[0]), int(point[1]), WHITE)
    current_coordinates = (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))
    gfxdraw.pixel(WIN, int(current_coordinates[0] + (WIDTH / 2)), current_coordinates[1], WHITE)
    iterations += 1
    subtitles()
    pygame.display.update()
    # clock.tick(fps)
            