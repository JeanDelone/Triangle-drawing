fps = "pomidor"
want_infinite_speed = "pomidor"
while want_infinite_speed != "y" and want_infinite_speed != "n":
    want_infinite_speed = input("Do you want to draw lines as fast as possible? (y/n): ")
    if want_infinite_speed != "y" and want_infinite_speed != "n":
        print("That's not a valid answer")
if want_infinite_speed == "n":
    try:
        fps = int(input("How many lines per second do you want to produce?: "))
    except ValueError:
        print("That's not an integer!")


def main():
    import pygame
    from pygame import gfxdraw
    import random
    from sys import exit

    

    WIDTH = 800
    HEIGHT = 450
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    PASTEL_BLUE = (109,207,246)

    POINT_A = (400,25)
    POINT_B = (200, 425)
    POINT_C = (600, 425)
    MIDDLE = ((POINT_A[0] + POINT_B[0] + POINT_C[0]) / 3, (POINT_A[1] + POINT_B[1] + POINT_C[1]) / 3) 

    POINTS = [POINT_A, POINT_B , POINT_C]

    current_coordinates = (400, 225)
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Infinite triangle')


    if want_infinite_speed == "n":
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            random_point = random.choice(POINTS)

            gfxdraw.pixel(WIN, int(POINT_A[0]), int(POINT_A[1]), WHITE)
            gfxdraw.pixel(WIN, int(POINT_B[0]), int(POINT_B[1]), WHITE)
            gfxdraw.pixel(WIN, int(POINT_C[0]), int(POINT_C[1]), WHITE)
            gfxdraw.pixel(WIN, 800, 450, WHITE)

            print(f"Random point: {random_point[0], random_point[1]}\nCurrent coordinates: {current_coordinates[0], current_coordinates[1]}")
            
            
            
            pygame.draw.line(WIN, random_color, current_coordinates, (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))) 
            current_coordinates = (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))
            
            
            
            print(f"New current_coordinates: {current_coordinates[0], current_coordinates[1]}\n_____________________")
            
            pygame.display.update()
            clock.tick(fps)
            
    else:
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            random_point = random.choice(POINTS)

            gfxdraw.pixel(WIN, int(POINT_A[0]), int(POINT_A[1]), WHITE)
            gfxdraw.pixel(WIN, int(POINT_B[0]), int(POINT_B[1]), WHITE)
            gfxdraw.pixel(WIN, int(POINT_C[0]), int(POINT_C[1]), WHITE)
            gfxdraw.pixel(WIN, 800, 450, WHITE)

            print(f"Random point: {random_point[0], random_point[1]}\nCurrent coordinates: {current_coordinates[0], current_coordinates[1]}")
            
            
            
            pygame.draw.line(WIN, random_color, current_coordinates, (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))) 
            current_coordinates = (int((current_coordinates[0] + random_point[0]) / 2), int((current_coordinates[1] + random_point[1]) / 2))
            
            
            
            print(f"New current_coordinates: {current_coordinates[0], current_coordinates[1]}\n_____________________")
            
            pygame.display.update()


if __name__ == "__main__":
    main()