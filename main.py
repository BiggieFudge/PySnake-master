# Import the pygame library and initialise the game engine
import pygame
import random
import time
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Open a new window
size = (900, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maman Sucks Dicks")


# The loop will carry on until the user exit the game (e.g. clicks the close button).
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


def init():
    x.clear()
    y.clear()
    x.append(random.randint(1, rows-2))
    y.append(random.randint(1, cols-2))
    Direction = 0
    snake_size = 1
    apple.append(random.randint(1, rows-2))
    apple.append(random.randint(1, cols-2))

def GenApple():
    apple[0] = random.randint(1, rows-2)
    apple[1] = random.randint(1, cols-2)

init()

font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render(str(snake_size), True ,(0,0,0))




start = 0
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Direction != 3:
                Direction = 1
            elif event.key == pygame.K_LEFT and Direction != 4:
                Direction = 2
            elif event.key == pygame.K_DOWN and Direction != 1:
                Direction = 3
            elif event.key == pygame.K_RIGHT and Direction != 2:
                Direction = 4
            if start == 0:
                start = time.time()
        # --- Game logic should go here
        #TODO Add Graphics
        #TODO Add powerup
        #TODO transparent walls
        def GetBigger():
            global snake_size
            snake_size += 1
            x.insert(0,apple[0])
            y.insert(0,apple[1])
            GenApple()
        def move():
            global snake_size
            if snake_size == 1:
                if Direction == 2:
                    if x[0] - 1 == apple[0] and y[0] == apple[1]:
                        GetBigger()
                    else:
                        x[0] = x[0] - 1
                elif Direction == 1:
                    if x[0] == apple[0] and y[0] - 1 == apple[1]:
                        GetBigger()
                    else:
                        y[0] = y[0] - 1
                elif Direction == 4:
                    if x[0] + 1 == apple[0] and y[0] == apple[1]:
                        GetBigger()
                    else:
                        x[0] = x[0] + 1
                elif Direction == 3:
                    if x[0] == apple[0] and y[0] + 1 == apple[1]:
                        GetBigger()
                    else:
                        y[0] = y[0] + 1
            else:
                if Direction == 2:
                    if x[0] - 1 == apple[0] and y[0] == apple[1]:
                        GetBigger()
                    else:
                        x.insert(0, x.pop(-1))
                        y.insert(0, y.pop(-1))
                        x[0] = x[1] - 1
                        y[0] = y[1]
                elif Direction == 1:
                    if x[0] == apple[0] and y[0] - 1 == apple[1]:
                        GetBigger()
                    else:
                        x.insert(0, x.pop(-1))
                        y.insert(0, y.pop(-1))
                        y[0] = y[1] - 1
                        x[0] = x[1]
                elif Direction == 4:
                    if x[0] + 1 == apple[0] and y[0] == apple[1]:
                        GetBigger()
                    else:

                        x.insert(0, x.pop(-1))
                        y.insert(0, y.pop(-1))
                        x[0] = x[1] + 1
                        y[0] = y[1]
                elif Direction == 3:
                    if x[0] == apple[0] and y[0] + 1 == apple[1]:
                        GetBigger()
                    else:
                        x.insert(0, x.pop(-1))
                        y.insert(0, y.pop(-1))
                        y[0] = y[1] + 1
                        x[0] = x[1]



            time.sleep(0.15)
            out_of_bounds()


        def out_of_bounds():
            global snake_size
            if x[0] > rows:
                exit(1)
            elif y[0] > cols:
                exit(1)
            elif x[0] == -2:
                exit(1)
            elif y[0] == -2:
                exit(1)
            for i in range(2, snake_size - 1):
                if x[i] == x[1] and y[i] == y[1]:
                    exit(1)


        # --- Drawing code should go here
        # First, clear the screen to white.

    screen.fill(WHITE)
    # The you can draw different shapes and lines or add text to your background stage.

    text = font.render(str(snake_size), True, (0, 0, 0))
    screen.blit(text, (0, 0))

    timer = font.render(str(time.time()-start), True, (0,0,0))
    screen.blit(timer, (800, 0))
    for index in range(snake_size):
        pygame.draw.rect(screen, BLACK, [x[index]*30, y[index]*30, 30, 30])
    pygame.draw.rect(screen, RED, [apple[0]*30, apple[1]*30, 30, 30])
    move()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()