import pygame
import tkinter
import sys
import time

root = tkinter.Tk()
root.withdraw()

pygame.init()
clock = pygame.time.Clock()

screen_width = 550
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sudoku Solver')

base_font = pygame.font.Font("Outfit.ttf", 25)
base_font1 = pygame.font.Font("Outfit-SemiBold.ttf", 33)
user_text = ''

input_rect = pygame.Rect(35, 50, 200, 27)
color_active = pygame.Color((190, 190, 190))
color_passive = pygame.Color((150, 150, 150))
color = color_passive

submit_rect = pygame.Rect(225, 120, 120, 45)
color_a = pygame.Color((190, 190, 190))
color_p = pygame.Color((140, 140, 140))
color_b = color_p
count_b = 0

active = False
ctrl = False
backsp = False
backsp_c = 0

array = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
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
        user_text = user_text[:-1]
        backsp_c += 1

    input_rect.centerx = screen_width/2
    submit_rect.centerx = screen_width/2

    pygame.draw.rect(screen, color_b, submit_rect, border_radius=2)
    pygame.draw.rect(screen, color, input_rect, width=0, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40)
  
    text_surface = base_font.render(user_text, True, (1, 1, 1))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y))
    text_surface_b = base_font1.render("Submit", True, (1, 1, 1))
    screen.blit(text_surface_b, (submit_rect.x+5, submit_rect.y+5))

    input_rect.w = max(480, text_surface.get_width()+10)

    pygame.display.update()
    clock.tick(60)