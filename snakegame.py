import pygame
import random
import os
pygame.mixer.init()


pygame.init()
#color
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (0,255,255)
yellow = (255,255,0)
magenta = (255,0,255)
#creating window
screen_width=900
screen_height=600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE KA KHEL")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
bgimg = pygame.image.load("download.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width, screen_height)).convert_alpha()

bgimg1 = pygame.image.load("windowimg.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(screen_width, screen_height)).convert_alpha()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
def plot_snake(gameWindow, color, snk_list, snake_size_x, snake_size_y):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size_x, snake_size_y])
def window():
    pygame.mixer.music.load('Window.mp3')
    pygame.mixer.music.play()
    exit_game = False
    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        high_score = f.read()
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(bgimg1, (0, 0))

        text_screen("  Welcome to snakegame  ",red,200,200)
        text_screen("PRESS SPACEBAR TO BEGIN", blue, 200, 300)
        text_screen("             Highscore:-  "+str(high_score),red,200,250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
        pygame.display.update()
        clock.tick(30)




#game loop
def game_loop():
    pygame.mixer.music.load('GameLoop.mp3')
    pygame.mixer.music.play()
    # game variables
    snk_list = []
    snk_lenght = 1
    exit_game = False
    game_over = False
    snake_x = random.randint(151, 599)
    snake_y = random.randint(101, 399)
    snake_size_x = 10
    snake_size_y = 12
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(151, 599)
    food_y = random.randint(101, 399)
    score = 0

    init_velocity = 5
    fps = 30

    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt","w") as f:
            f.write("0")


    with open("high_score.txt", "r") as f:
        high_score = f.read()
    highscore= int(high_score)
    while not exit_game:
        if game_over:
            pygame.mixer.music.load('GameOver.mp3')
            pygame.mixer.music.play()
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            gameWindow.fill(white)
            gameWindow.blit(bgimg1, (0, 0))

            text_screen("GAME-OVER", red, 330, 200)
            text_screen("PRESS ENTER TO CONTINUE",blue, 200, 350)
            text_screen("  Score:" + str(score), cyan, 350, 250)
            text_screen("HighScore:" + str(high_score), red, 330, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        window()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_q:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame. K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(150,600)
                food_y = random.randint(100, 400)
                snk_lenght += 10
                init_velocity +=0.5
                if (score > int(high_score)):
                    highscore= score
            gameWindow.fill(red)
            gameWindow.blit(bgimg,(0,0))
            pygame.draw.rect(gameWindow,blue,(150,100,600,400),5)
            text_screen("Score:" + str(score) + "HIGH_SCORE: "+str(highscore), white, 50, 50)
            pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size_x, snake_size_y])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
            if snake_x<150 or snake_x>740 or snake_y<100 or snake_y>490:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size_x, snake_size_y)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
window()
