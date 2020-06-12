"""
This program draws Serpinskyy's triangle drawn by chaotic method with Pygame library

----how-to-work-with-it----
In the start you have to match three dots, which would be the triangle's tops.
You're doing that by clicking to the  needed coordinates with your mouse's left button

Than program will start triangle's building from randomly chosen dot (marked in red)
"""

import pygame
import random
import sys

from pygame.locals import *
# importing libraries

pygame.init()  # Standart pygame initialisation

# ---RUN-PARAMETERS---
angles = 3  # Still doesn't work correctly with more angles (isn't like examples from google)
size = 1000  # setting window size
detalisation = 100000  # setting detalisation of image (number of dots)
# --------------------

win = pygame.display.set_mode((size, size), FULLSCREEN)  # Making window


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def GetPos(self):
        return self.x, self.y

    def Draw(self, color=(255, 255, 255), size=1):
        pygame.draw.rect(win, color, [self.x, self.y, size, size])
        pygame.display.update()


startdots = []
while len(startdots) < angles:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                startdots.append(Dot(event.pos[0], event.pos[1]))
    for dot in startdots:
        dot.Draw()


def main():
    startdot = Dot(random.randrange(0, size - 10), random.randrange(0, size - 10))
    startdot.Draw((255, 0, 0), 2)
    x, y = startdot.GetPos()

    for i in range(detalisation + 1):
        pygame.draw.rect(win, (0, 0, 0), [0, 0, 300, 30])
        win.blit(pygame.font.Font(None, 20).render(f'{i}/{detalisation}  Press "q" to quit', True, (255, 255, 255)), (5, 5))

        dx, dy = random.choice(startdots).GetPos()
        new_dot = Dot((x + (angles-2)*dx)/(angles-1), (y + (angles-2)*dy)/(angles-1))
        new_dot.Draw()

        x, y = new_dot.GetPos()

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()


main()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
