import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (52, 186, 52)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
DARK_RED = (163, 0, 29)
LIGHT_BLUE = (132, 255, 242)
GREY = (193, 193, 193)
BROWN = (173, 108, 55)
YELLOW = (252, 248, 22)
YELLOW2 = (255, 246, 170)
DARK_BLUE = (60, 61, 96)

# Game loop
done = False

stars = []
for i in range(100):
    x = random.randrange(0, 800)
    y = random.randrange(0, 500)
    r = random.randrange(1, 5)
    n = (x, y, r, r)
    stars.append(n)
    
rain = []
for i in range(500):
    x = random.randrange(0, 800)
    y = random.randrange(50, 500)
    r = random.randrange(1, 5)
    n = (x, y, r, r)
    rain.append(n)

cloud_locs = []
for i in range(20):
    x = random.randrange(0, 700)
    y = random.randrange(0, 50)
    loc = [x, y]
    cloud_locs.append(loc)

def draw_tree():
    pygame.draw.rect(screen, BROWN, [200, 450, 60, 50])
    pygame.draw.ellipse(screen, GREEN, [180, 300, 100, 175])  

def draw_cloud(loc):
    x, y = loc
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])

def draw_fence():
    y = 475
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])
    
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    ''' sky '''
    screen.fill(DARK_BLUE)

    ''' rain '''
    for n in rain:
        pygame.draw.ellipse(screen, BLUE, n)
        
    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW2, [700, -100, 200, 200])

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, YELLOW, s)
        
    ''' clouds '''
    for loc in cloud_locs:
        draw_cloud(loc)

    ''' trees '''
    draw_tree()
    
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 500, 800, 100])

    ''' house '''
    pygame.draw.rect(screen, DARK_RED, [500, 250, 200, 250])
    pygame.draw.polygon(screen, BLACK, [[600, 150], [480, 250], [720, 250]])
    pygame.draw.rect(screen, BROWN, [575, 450, 50, 50])

    ''' fence '''
    draw_fence()
            
    ''' angles for arcs are measured in radians (a pre-cal topic) '''

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
