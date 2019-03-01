

# [load modules here]
import sys
import pygame

from pygame.locals import *

# [resource handling functions here]

#class Ball:
    # [ball functions (methods) here]
    # [e.g. a function to calculate new position]
    # [and a function to check if it hits the side]

def main():
    # [initiate game environment here]
    pygame.init()

    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)

    DISPLAYSURFACE = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Hello World")

    DISPLAYSURFACE.fill(GREEN)

    rectangle = pygame.Rect(0, 0, 50, 50)

    pygame.draw.polygon(DISPLAYSURFACE, RED, ((0, 2), (9, 208), (9, 7), (150, 200)))


    # [create new object as instance of ball class]
#    ball = Ball()

    while True:
        # [check for user input]
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        pygame.display.update()

        # [call ball's update function]
        #ball.update()

if __name__ == '__main__':
    main()
