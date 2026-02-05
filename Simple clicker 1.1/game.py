import pygame; from random import randint; import sys
pygame.init()
click_sound = pygame.mixer.Sound("sounds/click.wav")
buy_s_sound = pygame.mixer.Sound("sounds/buy_s.wav")
buy_f_sound = pygame.mixer.Sound("sounds/buy_f.wav")
m_ch_sound = pygame.mixer.Sound("sounds/m_change.wav")
cas_win = pygame.mixer.Sound("sounds/cas_win.wav")
cas_lose = pygame.mixer.Sound("sounds/cas_lose.wav")
s_wid = 800; s_len = 600
screen = pygame.display.set_mode((s_wid, s_len))
pygame.display.set_caption("Simple clicker")

clock = pygame.time.Clock()

normal_font = pygame.font.Font(None, 36)
logo_font = pygame.font.Font(None, 72)

save_file = "save.txt"
def load_game():
    try:
        with open(save_file, "r") as f:
            points = int(f.readline())
            pts_gain = int(f.readline())
            c_u_p = int(f.readline())
        return points, pts_gain, c_u_p
    except FileNotFoundError:
        return 0, 1, 150
    
def save_game():
    with open(save_file, "w") as f:
        f.write(f"{points}\n{pts_gain}\n{c_u_p}")
        


running = True

game_state = "main"

points, pts_gain, c_u_p=load_game()
def h_or_t(bet):
    global points
    flip = randint(1,2)
    if flip == 2:
        points+=bet
        cas_win.play()
    else:
        points-=bet
        cas_lose.play()
        
while running:  
    
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT and game_state == "main":
                    points+=pts_gain
                    click_sound.play()
                    screen.blit(normal_font.render(f"Points: {points}", True, (255, 255, 255)), (50, 100))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game_state = "shop"    
                    m_ch_sound.play()
                if event.key == pygame.K_n:
                    game_state = "main"
                    m_ch_sound.play()
                if event.key == pygame.K_b:
                    game_state = "casino"
                    m_ch_sound.play()
                if event.key == pygame.K_1 and game_state == "shop" and points >= c_u_p:
                    buy_s_sound.play()
                    points-= c_u_p
                    c_u_p += 150
                    pts_gain += 1
                elif event.key == pygame.K_1 and game_state == "shop" and points < c_u_p:
                    buy_f_sound.play()       
                if event.key == pygame.K_1 and game_state == "casino" and points >= 100:
                    h_or_t(100)
                elif event.key == pygame.K_2 and game_state == "casino" and points >= 500:
                    h_or_t(500)
                elif event.key == pygame.K_3 and game_state == "casino" and points >= 500:
                    h_or_t(1000)
        
            
        if game_state == "main":
            screen.blit(normal_font.render("Main", True, (255, 255, 255)), (50, 375))
            screen.blit(normal_font.render("Press M for shop", True, (150, 150, 150)), (50, 410))
            screen.blit(normal_font.render("Press B for casino", True, (150, 150, 150)), (50, 445))
            screen.blit(normal_font.render(f"Points: {points}", True, (255, 255, 255)), (50, 100))
            screen.blit(normal_font.render(f"Points gain: {pts_gain}", True, (255, 255, 255)), (50, 150))
            screen.blit(logo_font.render("Simple clicker", True, (255, 255, 255)), (5, 550))
        
        elif game_state == "shop":
            screen.blit(normal_font.render("Shop", True, (255, 255, 255)), (50, 375))
            screen.blit(normal_font.render("Press N for menu", True, (150, 150, 150)), (50, 410))
            screen.blit(normal_font.render(f"1. +1 to your clicks! Price: {c_u_p} points", True, (255, 255, 255)), (50, 100))
            screen.blit(logo_font.render("Simple clicker", True, (255, 255, 255)), (5, 550))
            
        elif game_state == "casino":
            screen.blit(normal_font.render("HEADS OR TAILS.", True, (255, 255, 0)), (280, 100))
            screen.blit(normal_font.render("1. Bet 100", True, (255, 255, 255)), (100, 150))
            screen.blit(normal_font.render("2. Bet 500", True, (255, 255, 255)), (100, 200))
            screen.blit(normal_font.render("3. Bet 1000", True, (255, 255, 255)), (100, 250))
            screen.blit(logo_font.render("Simple clicker", True, (255, 255, 255)), (5, 550))
            screen.blit(normal_font.render(f"Points: {points}", True, (255, 255, 255)), (50, 100))
            screen.blit(normal_font.render("Press N for menu", True, (150, 150, 150)), (50, 410))
            screen.blit(normal_font.render("Casino", True, (255, 255, 255)), (50, 375))
            
        pygame.display.flip()
            
            
        clock.tick(30)
            
   
        
        

            