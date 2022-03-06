
from cmath import sqrt
from turtle import color, distance
import pygame
import pygments
import random
import math

# Initialize the PyGame
pygame.init()


# Create the Screen
screen = pygame.display.set_mode((800, 600))


# Background
background = pygame.image.load('J:/Programming/Python/PyGame/Space_Invader/images/background.jpg')


# Title and Logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('J:/Programming/Python/PyGame/Space_Invader/images/logo.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('J:/Programming/Python/PyGame/Space_Invader/images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('J:/Programming/Python/PyGame/Space_Invader/images/ghost.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.4)
    enemyY_change .append(40)

# Bullet
# Ready -> Can not see the bullet at start
# Fire -> The bullet is currently moving
bulletImg = pygame.image.load('J:/Programming/Python/PyGame/Space_Invader/images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.7
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemY, bulletX, bulletY):
    value = math.pow(bulletX-enemyX, 2) + math.pow(bulletY-enemY, 2)
    distance = math.sqrt(value)
    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score =  font.render("Score: " +  str(score_value), True, (250,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))  
    # RGB (Red, Green, Blue) Colour Co-ordinate

    # Background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Quit functionality
            running = False

    # If key stroke is pressed left  or right
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                # print("Left arrow is pressed")
                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:
                # print("Right arrow is pressed")
                playerX_change = 0.5

            if event.key == pygame.K_SPACE:
                # print("Right arrow is pressed")
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                # print("Keystoke has been released")
                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

    # Update the value before calling the function
    playerX += playerX_change

    # Boundary Condition
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Updating value of enemy co-ordinate
    for i in range(no_of_enemies):

        # Game Over
        if enemyY[i] >420:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]
        elif enemyY[i] >= 415:
            enemyY[i] = random.randint(50,150)

            # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <=0:
        bulletY=480
        bullet_state = "ready"

    

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
