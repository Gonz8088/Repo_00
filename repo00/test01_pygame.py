# The basic Pygame game
# From: https://www.pygame.org/docs/tut/tom_games2.html#makegames-2

import pygame
from pygame.locals import *    # This is optional

class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((450, 250))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Display Caption')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((128, 128, 128))

    # Display some text
    # font = pygame.font.Font(None, 50)
    # text = font.render("Rendered Text", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # background.blit(text, textpos)

    # Load and display an image
    smileyface = pygame.image.load('smileyface.bmp')
    smileyface_rect = smileyface.get_rect()
    smileyface_rect.midbottom = screen_rect.midbottom

    ball = Ball()

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    smileyface_rect.x += 1
                elif event.key == pygame.K_LEFT:
                    smileyface_rect.x -= 1
                elif event.key == pygame.K_UP:
                    smileyface_rect.y -= 1
                elif event.key == pygame.K_DOWN:
                    smileyface_rect.y += 1
        screen.blit(background, (0, 0))
        screen.blit(smileyface, smileyface_rect)
        pygame.display.flip()

        ball.update()

if __name__ == '__main__':
    main()
