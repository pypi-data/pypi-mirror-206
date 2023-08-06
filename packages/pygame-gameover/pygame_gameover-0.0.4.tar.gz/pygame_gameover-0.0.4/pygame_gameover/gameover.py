import pygame
from pygame import mixer
import sys
import os





def gameover():
    screen=pygame.display.set_mode((1500,800))
    gameover_exit=False
    pygame.font.init()
    mixer.init()
    pygame.display.set_caption("GAMEOVER")
    gameover_img=pygame.image.load(os.path.join("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\heart.png"))
    pygame.display.set_icon(gameover_img)
    big_font=pygame.font.Font(None,200)
    mid_font=pygame.font.Font(None,80)
    small_font=pygame.font.Font(None,60)
    white=(255,255,255)
    red=(255,0,0)
    green=(0,255,255)
    blue=(0,0,255)
    yellow=(255,255,0)
    black=(0,0,0)
    gray=(128,128,128)

    pygame.mixer.music.load(os.path.join("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\hit.wav"))
    pygame.mixer.music.play()
    gameover_sound=mixer.Sound(os.path.join("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\You_Lose_Sound_Effect(256k).mp3"))
    gameover_sound.play()
    # re try data
    re_try=mid_font.render("    TRY AGAIN ",True,gray)
    re_try_x=450
    re_try_y=200
    re_try_collision=pygame.Rect(re_try_x,re_try_y,400,100)
    # exit data
    exits=mid_font.render("        EXIT",True,gray)
    exit_x=450
    exit_y=330
    exit_collisoin=pygame.Rect(exit_x,exit_y,400,100)
    gameover_text=big_font.render("  GAME OVER ",True,red)
    while gameover_exit==False:
        mouse=pygame.mouse.get_pos()
        # new rect
        mouse__rect=pygame.Rect(mouse[0],mouse[1],20,10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if re_try_collision.colliderect(mouse__rect):
                    if event.button==1:
                        gameover_exit=True
                if exit_collisoin.colliderect(mouse__rect):
                    if event.button==1:
                        gameover_exit=True
                        sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE or event.key==pygame.K_RETURN:
                    gameover_exit=True
                
                    
        screen.fill(white)
        # re try
        pygame.draw.rect(screen,black,(re_try_x,re_try_y,400,100))
        
        screen.blit(re_try,(re_try_x,re_try_y+20))
        
        # exit 
        pygame.draw.rect(screen,black,(exit_x,exit_y,400,100))
        screen.blit(exits,(exit_x,exit_y+20))
        # gameover text
        screen.blit(gameover_text,(240,20))
        
        pygame.display.flip()
