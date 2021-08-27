# Import the pygame library and initialise the game engine
import pygame
import random
import time
import os     #  --change to fixed directory

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Open a new window
size = (900, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FUN SNAKE")


choice1 = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\choice.png')
choice2 = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\choice.png')
b1 = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\button1.png')
b2 = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\button2.png')
b3 = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\button3.png')
fixedwalls = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\button_Fixed_Walls.png')
transwalls = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\button_go-through-walls.png')
play = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\button_play.png')
choiceplay = pygame.image.load(r'D:\Visual Studio repos\PySnake-master\sprites\choiceplay.png')

carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
x = []
y = []
snake_size = 1
Direction = 0
rows = 900/30
cols = 900/30
apple = []
choice = 1
choicediff = 1
choicewalls = 1

def genrate_apple():
    apple[0] = random.randint(1, rows-2)
    apple[1] = random.randint(1, cols-2)
    if apple[0] in x and apple[1] in y:
        genrate_apple()


def init():
    x.clear()
    y.clear()
    x.append(random.randint(1, rows-2))
    y.append(random.randint(1, cols-2))
    Direction = 0
    snake_size = 1
    apple.append(random.randint(1, rows-2))
    apple.append(random.randint(1, cols-2))


def menu():
    global choice, choicediff , choicewalls
    animateup = 246
    animatedown = 496
    up = 1
    global clock
    carrymenu = True
    while carrymenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carrymenu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and choice < 3:
                    choice += 1
                if event.key == pygame.K_UP and choice > 1:
                    choice -= 1
                if event.key == pygame.K_RIGHT and choice == 1 and choicediff < 3:
                    choicediff += 1
                if event.key == pygame.K_LEFT and choice == 1 and choicediff > 1:
                    choicediff -= 1
                if event.key == pygame.K_RIGHT and choice == 2 and choicewalls < 2:
                    choicewalls += 1
                if event.key == pygame.K_LEFT and choice == 2 and choicewalls > 1:
                    choicewalls -= 1
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    carrymenu = False

        screen.fill(WHITE)

        if choice == 3:
            screen.blit(choiceplay, (293, 695))
        screen.blit(choice1, (45 + (300 * (choicediff-1)), animateup))
        screen.blit(choice2, (95 + (500 * (choicewalls - 1)), animatedown))
        screen.blit(b1, (50,250))
        screen.blit(b2, (350, 250))
        screen.blit(b3, (650, 250))
        screen.blit(fixedwalls, (100, 500))
        screen.blit(transwalls, (600, 500))
        screen.blit(play, (300, 700))
        pygame.display.flip()
        if choice == 1:
            if animateup == 244:
                up = 1
            elif animateup == 250:
                up = 0
            if animateup < 250 and up == 1:
                animateup += 0.5
            else:
                animateup -= 0.5
        elif choice == 2:
            if animatedown == 494:
                up = 1
            elif animatedown == 500:
                up = 0
            if animatedown < 500 and up == 1:
                animatedown += 0.5
            else:
                animatedown -= 0.5


        clock.tick(60)


init()
font = pygame.font.Font('freesansbold.ttf', 32)  # create a text surface object,
# on which text is drawn on it.
menu()


def getbigger():     #  Snake Eating Apple
    global snake_size
    snake_size += 1
    x.insert(0, apple[0])
    y.insert(0, apple[1])
    genrate_apple()


start = 0


def starttime():
    global start
    if start == 0:
        start = time.time()

def move():
    global snake_size

    if snake_size == 1 and Direction != 0:
        starttime()
        if Direction == 2:
            if x[0] - 1 == apple[0] and y[0] == apple[1]:
                getbigger()
            else:
                x[0] = x[0] - 1
        elif Direction == 1:
            if x[0] == apple[0] and y[0] - 1 == apple[1]:
                getbigger()
            else:
                y[0] = y[0] - 1
        elif Direction == 4:
            if x[0] + 1 == apple[0] and y[0] == apple[1]:
                getbigger()
            else:
                x[0] = x[0] + 1
        elif Direction == 3:
            if x[0] == apple[0] and y[0] + 1 == apple[1]:
                getbigger()
            else:
                y[0] = y[0] + 1
    elif Direction != 0:
        starttime()
        if Direction == 2:
            if x[0] - 1 == apple[0] and y[0] == apple[1]:  # eats an apple
                getbigger()
            else:
                x.insert(0, x.pop(-1))
                y.insert(0, y.pop(-1))
                x[0] = x[1] - 1
                y[0] = y[1]
        elif Direction == 1:
            if x[0] == apple[0] and y[0] - 1 == apple[1]:
                getbigger()
            else:
                x.insert(0, x.pop(-1))
                y.insert(0, y.pop(-1))
                y[0] = y[1] - 1
                x[0] = x[1]
        elif Direction == 4:
            if x[0] + 1 == apple[0] and y[0] == apple[1]:
                getbigger()
            else:
                x.insert(0, x.pop(-1))
                y.insert(0, y.pop(-1))
                x[0] = x[1] + 1
                y[0] = y[1]
        elif Direction == 3:
            if x[0] == apple[0] and y[0] + 1 == apple[1]:
                getbigger()
            else:
                x.insert(0, x.pop(-1))
                y.insert(0, y.pop(-1))
                y[0] = y[1] + 1
                x[0] = x[1]

    time.sleep(0.25 / choicediff)


def out_of_bounds():  # EndGame
    global snake_size
    if choicewalls == 1:
        if x[0] >= rows:
            exit(1)
        elif x[0] < 0:
            exit(1)
        if y[0] >= cols:
            exit(1)
        elif y[0] < 0:
            exit(1)
    else:
        if x[0] == rows:
            x[0] = 0
        elif x[0] == -1:
            x[0] = rows-1
        if y[0] == cols:
            y[0] = 0
        elif y[0] == -1:
            y[0] = cols - 1
    for i in range(1, snake_size - 1):
        if x[i] == x[0] and y[i] == y[0]:
            exit(1)




#  def pausegame()

game_state= True #   {True - for running, False - for pause
pause_time = 0
while carryOn:

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and start != 0:
                if game_state:
                    game_state = False
                else:
                    game_state = True
            if event.key == pygame.K_UP and Direction != 3:
                Direction = 1
                break
            elif event.key == pygame.K_LEFT and Direction != 4:
                Direction = 2
                break
            elif event.key == pygame.K_DOWN and Direction != 1:
                Direction = 3
                break
            elif event.key == pygame.K_RIGHT and Direction != 2:
                Direction = 4
                break


        # TODO Add Graphics
        #TODO Add powerup
        #TODO Add pause game
        #TODO 31 long



        # --- Drawing code should go here
    screen.fill(WHITE)   # First, clear the screen to white.
    if game_state:

        # The you can draw different shapes and lines or add text to your background stage.

        text = font.render(str(snake_size), True, (0, 0, 0))
        screen.blit(text, (0, 0))
        stopwatch = time.time() - start
        if start==0:
            stopwatch= 0
        timer = font.render(str("%d" %(stopwatch - pause_time)), True, (0,0,0))
        screen.blit(timer, (800, 0))
        for index in range(snake_size):
            pygame.draw.rect(screen, BLACK, [x[index]*30, y[index]*30, 30, 30])  #  print snake
        pygame.draw.rect(screen, RED, [apple[0]*30, apple[1]*30, 30, 30])   #  print apple
        move()
        pygame.display.flip()
        out_of_bounds()
        # --- Go ahead and update the screen with what we've drawn.
    else:
        text = font.render("Paused", True , (0,0,0))
        screen.blit(text,(380 ,420))
        pygame.display.flip()
        pause_time =time.time() -(start +stopwatch)

    clock.tick(60)  # --- Limit to 60 frames per second

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()