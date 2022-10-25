import pygame
import tkinter
import sys
import time
import os

#os.chdir(r"C:\Users\Prisha\Desktop\Prisha\Python\TS\Velocity Sudoku solver\Velocity_prog-main")

root = tkinter.Tk()
root.withdraw()

pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sudoku Solver')

base_font = pygame.font.Font("Outfit.ttf", 25)
base_font1 = pygame.font.Font("Outfit-SemiBold.ttf", 20)
navbar_font = pygame.font.Font("dosis.ttf", 42)
sud_font = pygame.font.Font(None, 35)
user_text = ''

navbar_rect = pygame.Rect(0, 0, 600, 42)

sudx, sudy = 80, 75

input_rect = pygame.Rect(32, 550, 200, 27)
color_active = pygame.Color((190, 190, 190))
color_passive = pygame.Color((150, 150, 150))
color = color_passive

submit_rect = pygame.Rect(482, 552, 80, 23)
color_a = pygame.Color((140, 140, 140))
color_p = pygame.Color((110, 110, 110))
color_b = color_p
count_b = 0

active = False
ctrl = False
backsp = False
infoclick = False
backsp_c = 0
copy = True
sud = False
array = ""
grid = [[0,0,7,0,4,0,0,0,0],
[0,0,0,0,0,8,0,0,6],
[0,4,1,0,0,0,9,0,0],
[0,0,0,0,0,0,1,7,0],
[0,0,0,0,0,6,0,0,0],
[0,0,8,7,0,0,2,0,0],
[3,0,0,0,0,0,0,0,0],
[0,0,0,1,2,0,0,0,0],
[8,6,0,0,7,0,0,0,5]]

LIGHTGREY = (110, 110, 110)
LIME = (0, 255, 21)
DARKGREY = (90, 90 , 90)
infocir = pygame.draw.ellipse (screen, LIME, [10, 5, 30,30], 3)
wallcir = pygame.draw.rect (screen, LIME, [558, 5, 30, 30], 3)

sudokuempty = pygame.image.load("empty_sudoku_board.png")
info = pygame.image.load("icon_info.png")
wall  = pygame.image.load("icon_bg.png")
sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
info = pygame.transform.scale(info, [32, 32])
wall = pygame.transform.scale(wall, [32, 32])

#text_width, text_height = base_font.size(user_text)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if input_rect.collidepoint(event.pos):
                active = True
            elif not input_rect.collidepoint(event.pos):
                active = False
            else:
                active = False
            if submit_rect.collidepoint(event.pos):
                array = user_text
                user_text = ""
                color_b = color_a
                count_b = 0
                sud = True
            if infocir.collidepoint(event.pos):
                infoclick = True
            if not infocir.collidepoint(event.pos):
                infoclick = False

            if wallcir.collidepoint(event.pos):
                print("wall")
        if event.type == pygame.KEYDOWN:
            if not active:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif active:
                if event.key == pygame.K_BACKSPACE:
                    backsp = True
                elif (event.key == pygame.K_LCTRL) or (event.key == pygame.K_RCTRL):
                    ctrl = True
                elif ctrl:
                    if event.key == pygame.K_v:
                        user_text += root.clipboard_get()
                        copy = True
                else:
                    user_text += event.unicode
        if event.type == pygame.KEYUP:
            if active:
                if (event.key == pygame.K_LCTRL) or (event.key == pygame.K_RCTRL):
                    ctrl = False
                if event.key == pygame.K_BACKSPACE:
                    backsp = False
                    backsp_c = 0
    
    screen.fill((50, 50, 50))
    if active:
        color = color_active
    else:
        color = color_passive

    if count_b > 10:
        color_b = color_p
        count_b = 0
    count_b += 1
    if backsp:
        if backsp_c < 2:
            time.sleep(0.13)
        else:
            time.sleep(0.03)
        user_text = temp[:-1]
        temp = temp[:-1]
        backsp_c += 1

    input_rect.centerx = screen_width/2
    
    if len(user_text) > 1:
        if copy:
            array = user_text
            temp = array
            copy = False
    text_width, text_height = base_font.size(user_text)
    screen.blit(sudokuempty, [75, 70])
    
    for i in range(100000):
        if text_width > 440:
            user_text = user_text[:-1]
        else:
            text_surface = base_font.render(user_text, True, (1, 1, 1))

            break
        break
   
    
    pygame.draw.rect(screen, color, input_rect, width=0, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40) #input button  
    screen.blit(text_surface, (input_rect.x+5, input_rect.y))

    pygame.draw.rect(screen, color_b, submit_rect, border_radius=20)
    text_surface_b = base_font1.render("Submit", True, (1, 1, 1))
    screen.blit(text_surface_b, (submit_rect.x+7, submit_rect.y+2))

    pygame.draw.rect(screen, LIGHTGREY, navbar_rect, border_bottom_left_radius=5, border_bottom_right_radius=5)
    text_navbar = navbar_font.render("Sudoku Solver", True, (0, 200, 255))
    screen.blit(text_navbar, (180, -5))

    screen.blit(wall, [558, 5])
    screen.blit(info, [10, 5])
    input_rect.w = 530
    sudx, sudy = 93, 85
    # Ek min de mai net dekhta yeh karne de pehle
    if sud:
        grid = eval(array)
        for i in grid:
            for f in i:
                if f == 0:
                    f = " "
                text_sud = sud_font.render(str(f), True, (0, 0, 0))
                screen.blit(text_sud, (sudx, sudy))
                sudx += 50
            sudx = 93
            sudy += 50

    if infoclick:
        pygame.draw.rect(screen, DARKGREY, [50,50   , 375, 170])
    pygame.display.update()
    clock.tick(60)