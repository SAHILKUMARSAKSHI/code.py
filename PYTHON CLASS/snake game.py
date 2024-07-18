import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set clock for controlling the speed of the game
clock = pygame.time.Clock()

# Set font for displaying score
font_style = pygame.font.SysFont(None, 50)

# Define function for displaying score
def score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Define function for drawing snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], block_size, block_size])

# Define function for the main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Set starting position and dimensions of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2
    snake_block = 10
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1

    # Set starting position of food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update snake's position
        x1 += x1_change
        y1 += y1_change

        # Check if the snake has hit the boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake has eaten food
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten food, and if so, respawn food and increase snake length
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

gameLoop()
