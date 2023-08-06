

## Installation
```pip install pygame_pause```

## How to use it?

import pygame
import sys
import os 
"""first just import the module"""
from pygame_pause import pause  






pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.init()
screen=pygame.display.set_mode((1500,800),pygame.RESIZABLE)
pygame.display.set_caption('pause module example')
clock=pygame.time.Clock()
fps=60
def gameloop():
    x=100
    x_vol=0
    y=200
    y_vol=0
    
    while True:
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    """second just call the module"""
                    pause.pause(gameloop)
                if event.key==pygame.K_RIGHT:
                    x_vol=10
                if event.key==pygame.K_LEFT:
                    x_vol=-10
                if event.key==pygame.K_UP:
                    y_vol=-10
                if event.key==pygame.K_DOWN:
                    y_vol=10
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    x_vol=0
                if event.key==pygame.K_LEFT:
                    x_vol=0
                if event.key==pygame.K_UP:
                    y_vol=0
                if event.key==pygame.K_DOWN:
                    y_vol=0



        x+=x_vol
        y+=y_vol

        screen.fill((255,255,255))
        mouse_rect=pygame.draw.rect(screen,(0,0,255),(x,y,100,50))
        clock.tick(fps)
        pygame.display.flip()

gameloop()


## License

© 2023 KURBAN HUSSAIN

This repository is licensed under the MIT license. See LICENSE for details.
