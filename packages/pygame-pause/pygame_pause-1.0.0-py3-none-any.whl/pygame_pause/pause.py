import pygame
import sys
import os 
from pygame import mixer



pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.init()
screen=pygame.display.set_mode((1500,800),pygame.RESIZABLE)
def pause(gameloop):
    # creat the font

    big_font=pygame.font.Font(None,100)
    mid_font=pygame.font.Font(None,70)
    # pause text
    pause_text=big_font.render("   PAUSE",True,(255,165,0))
    # button sound
    pause_sound=mixer.Sound(os.path.join('pics','shuriken.wav'))
    

    # tile
    pygame.display.set_caption('pause')
    icon_pause=pygame.image.load(os.path.join('pics','pause image.png'))
    
    
    
    pygame.display.set_icon(icon_pause)
    # play data
    
    play_x=645
    play_y=236
    play_text=mid_font.render("PLAY",True,(128,128,128))
    play_collision=pygame.Rect(play_x,play_y,300,100)

    # restart data
    
    restart_x=645
    restart_y=368
    restart_text=mid_font.render("RESTART",True,(128,128,128))
    restart_collision=pygame.Rect(restart_x,restart_y,300,100)
    # exit
    
    exit_x=645
    exit_y=498
    exit_text=mid_font.render("EXIT",True,(128,128,128))
    exit_collision=pygame.Rect(exit_x,exit_y,300,100)
    pause_game_exit=True
    while pause_game_exit:
        mouse=pygame.mouse.get_pos()
        mouse_rect=pygame.Rect(mouse[0],mouse[1],10,10)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pause_game_exit=False
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pause_game_exit=False
                    sys.exit()
                elif event.key==pygame.K_q:
                    pause_game_exit=False
                    sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if mouse_rect.colliderect(play_collision):
                    if event.button==1:
                        pause_sound.play()
                        pause_game_exit=False
                elif mouse_rect.colliderect(restart_collision):
                    if event.button==1:
                        pause_sound.play()
                        gameloop()
                elif mouse_rect.colliderect(exit_collision):
                    if event.button==1:
                        pause_sound.play()
                        pause_game_exit =False
                        sys.exit()




        screen.fill((255,255,255))
        if mouse_rect.colliderect(play_collision):
            pygame.draw.rect(screen,(0,255,0),(play_x,play_y,300,100))
            pygame.draw.rect(screen,(0,0,0),(restart_x,restart_y,300,100))
            # draw exit button
            pygame.draw.rect(screen,(0,0,0),(exit_x,exit_y,300,100))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_rect.colliderect(restart_collision):
            pygame.draw.rect(screen,(255,165,0),(restart_x,restart_y,300,100))
            # draw play button
            pygame.draw.rect(screen,(0,0,0),(play_x,play_y,300,100))
            # draw exit button
            pygame.draw.rect(screen,(0,0,0),(exit_x,exit_y,300,100))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_rect.colliderect(exit_collision):
            pygame.draw.rect(screen,(255,0,0),(exit_x,exit_y,300,100))
            # draw play button
            pygame.draw.rect(screen,(0,0,0),(play_x,play_y,300,100))
            # draw restatr button
            pygame.draw.rect(screen,(0,0,0),(restart_x,restart_y,300,100))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            # draw play button
            pygame.draw.rect(screen,(0,0,0),(play_x,play_y,300,100))
            # draw restatr button
            pygame.draw.rect(screen,(0,0,0),(restart_x,restart_y,300,100))
            # draw exit button
            pygame.draw.rect(screen,(0,0,0),(exit_x,exit_y,300,100))

        





        # play text
        screen.blit(play_text,(play_x+80,play_y+25))
        
        # restart text
        screen.blit(restart_text,(restart_x+40,restart_y+25))
        
        # exit text
        screen.blit(exit_text,(exit_x+80,exit_y+25))

        # pause text
        screen.blit(pause_text,(600,40))

        
        pygame.display.flip()  




        

