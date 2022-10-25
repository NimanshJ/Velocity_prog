import pygame
import tkinter
import sys
import time
import webbrowser

def sol(grid, hori, vert, num):
    for a in range(9):
        if grid[hori][a] == num:
            return False
    for a in range(9):
        if grid[a][vert] == num:
            return False
    startHori = hori - hori % 3
    startVert = vert - vert % 3
    for q in range(3):
        for r in range(3):
            if grid[q + startHori][r + startVert] == num:
                return False
    return True

def sud(grid, hori, vert):
    if (hori == 9 - 1 and vert == 9):
        return True
    if vert == 9:
        hori += 1
        vert = 0
    if grid[hori][vert] > 0:
        return sud(grid, hori, vert + 1)
    for num in range(1, 10, 1):
        if sol(grid, hori, vert, num):
            grid[hori][vert] = num
            if sud(grid, hori, vert + 1):
                return True
        grid[hori][vert] = 0

root = tkinter.Tk()
root.withdraw()

pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sudoku Solver')

base_font = pygame.font.Font("Rubik-VariableFont_wght.ttf", 20)
base_font1 = pygame.font.Font("Rubik-VariableFont_wght.ttf", 13)
base_font2 = pygame.font.Font("Rubik-VariableFont_wght.ttf", 17)
navbar_font = pygame.font.Font("Rubik-Bold.ttf", 35)
sud_font = pygame.font.Font(None, 35)
user_text = ''

navbar_rect = pygame.Rect(0, 0, 600, 42)

sudx, sudy = 80, 75

input_rect = pygame.Rect(32, 550, 200, 32)
color_active = pygame.Color((190, 190, 190))
color_passive = pygame.Color((150, 150, 150))
color = color_passive

submit_rect = pygame.Rect(482, 552, 80, 23)
color_a = pygame.Color((140, 140, 140))
color_p = pygame.Color((110, 110, 110))
color_b = color_p
count_b = 0

solve_rect = pygame.Rect(482, 600, 80, 23)
pygame.draw.rect(screen, color_b, submit_rect, border_radius=20)
active = False
ctrl = False
backsp = False
infoclick = False
backsp_c = 0
copy = True
sud1 = False
count_sud = 0
array = ""
grid = ""
col = 0

LIME = (0, 255, 21)
LIGHTYELLOW = (252, 229, 202)
RED = (204, 111, 106)
LG = (202,252,207)
DG = (135, 168, 139)
LB = (202, 234, 252)
DB = (135, 156, 168)
LP = (252, 202, 202)
DP = (181, 137, 137)
LBG = (180, 255, 232)
DPU = (139, 165, 173)

wallcir = pygame.draw.rect (screen, LIME, [495, 17, 100, 20], 3)
infocir = pygame.draw.rect (screen, LIME, [5, 20, 100,20], 3)
sudokuempty = pygame.image.load("empty_sudoku_board.png")
sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
solve_rect = pygame.draw.rect(screen,LIME,(270, 600, 60,20))

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
                user_text = ""
                color_b = color_a
                count_b = 0
                count_sud = 0
                sud1 = True
            if infocir.collidepoint(event.pos):
                webbrowser.open_new('https://docs.google.com/document/d/1Q7CcOne9C1ZnbDKjuZg4GxKqMoB_qysEYL3IcXjv3pw/edit')
                

            if not infocir.collidepoint(event.pos):
                infoclick = False
            if wallcir.collidepoint(event.pos):
                if not col == 4:
                    col +=1
                else:col=0

            if solve_rect.collidepoint(event.pos):
                sud(grid, 0, 0)
                sud1 = 1
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
    if col == 0:
        info = base_font1.render("HOW TO PLAY?", True, RED)
        wall = base_font1.render("SWITCH COLOR", True, RED)
        solve = base_font2.render("SOLVE", True, RED)
        sudokuempty = pygame.image.load("empty_sudoku_board.png")
        sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
        text_surface_b = base_font2.render("SUBMIT", True, RED)
        text_navbar = navbar_font.render("SUDOKU SOLVER", True, RED)
        screen.fill(LIGHTYELLOW)
        pygame.draw.rect(screen, RED, input_rect, width=3, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40) #input button  
    elif col == 1:
        info = base_font1.render("HOW TO PLAY?", True, DG)
        wall = base_font1.render("SWITCH COLOR", True, DG)
        solve = base_font2.render("SOLVE", True, DG)
        sudokuempty = pygame.image.load("su1.png")
        sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
        text_surface_b = base_font2.render("SUBMIT", True, DG)
        text_navbar = navbar_font.render("SUDOKU SOLVER", True, DG)
        screen.fill(LG)
        pygame.draw.rect(screen, DG, input_rect, width=3, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40) #input button  
    elif col == 2:
        info = base_font1.render("HOW TO PLAY?", True, DB)
        wall = base_font1.render("SWITCH COLOR", True, DB)
        solve = base_font2.render("SOLVE", True, DB)
        sudokuempty = pygame.image.load("su3.png")
        sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
        text_surface_b = base_font2.render("SUBMIT", True, DB)
        text_navbar = navbar_font.render("SUDOKU SOLVER", True, DB)
        screen.fill(LB)
        pygame.draw.rect(screen, DB, input_rect, width=3, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40) #input button  
    elif col == 3:
        info = base_font1.render("HOW TO PLAY?", True, DP)
        wall = base_font1.render("SWITCH COLOR", True, DP)
        solve = base_font2.render("SOLVE", True, DP)
        sudokuempty = pygame.image.load("Picture1.png")
        sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
        text_surface_b = base_font2.render("SUBMIT", True, DP)
        text_navbar = navbar_font.render("SUDOKU SOLVER", True, DP)
        screen.fill(LP)
        pygame.draw.rect(screen, DP, input_rect, width=3, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40) #input button  
    elif col == 4:
        info = base_font1.render("HOW TO PLAY?", True, DPU)
        wall = base_font1.render("SWITCH COLOR", True, DPU)
        solve = base_font2.render("SOLVE", True, DPU)
        sudokuempty = pygame.image.load("su5.png")
        sudokuempty = pygame.transform.scale(sudokuempty, [450, 450])
        text_surface_b = base_font2.render("SUBMIT", True, DPU)
        text_navbar = navbar_font.render("SUDOKU SOLVER", True, DPU)
        screen.fill(LBG)
        pygame.draw.rect(screen, DPU, input_rect, width=3, border_radius=20, border_top_left_radius=40, border_top_right_radius=40, border_bottom_left_radius=40, border_bottom_right_radius=40) #input button  
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
  
    screen.blit(text_surface, (input_rect.x+10, input_rect.y+3))
   
    screen.blit(text_surface_b, (submit_rect.x+7, submit_rect.y+2))

    screen.blit(text_navbar, (160, 5))
    
    screen.blit(solve, (275, 600))
    

    screen.blit(wall, [500, 20])
    screen.blit(info, [10, 20])
    input_rect.w = 530
    sudx, sudy = 93, 85

    if sud1:
        if count_sud < 1:
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
        count_sud += 1

    pygame.display.update()
    clock.tick(60)