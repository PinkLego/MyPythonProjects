import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Dectection')

# Set up the color.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
     
# Set up movement varibles.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6


# Run the game loop.
while True:
    # Check for event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard varibles.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == k_d:
                moveLeft = False
                moveRight = True
            if event.type == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K.DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight == False
            if event.key == K_UP or event.key == K_w:
                moveUp == False
            if event.key == K_DOWN or event_key == K_s:
                moveDown == False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.left)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foodS.append(pygame.Rect(event.pos[0], FOODSIZE, FOODSIZE))
    
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.
    if moveDown and  player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.Left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right = WINDOWHEIGHT:
        player.right += MOVESPEED

        # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player)

    # Check whether the player has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # Draw the food.
    for i in range(len(food)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40)