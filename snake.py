import pygame
import random

width, height = 630, 480
row, column = 30, 40
fps = 10

# snake and apple
snake_dir =''
snake_list = []
apple_pos = []
snake_eat = False
snake_dead = False
score = 0

def snake_generate(SnakeList, SnakeDir):
    if len(SnakeList) == 0:
        # head
        x = random.randrange(3, column - 1)
        y = random.randrange(3, row - 1)
        SnakeList.append([x, y])

        # body
        SnakeList.append(random.choice([[x-1, y], [x+1, y], [x, y-1], [x, y+1]]))

        # tail
        x = SnakeList[-1][0]
        y = SnakeList[-1][1]
        temp = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        temp.remove([SnakeList[0][0], SnakeList[0][1]])
        SnakeList.append(random.choice(temp))
    
    if len(SnakeDir) == 0:
        # init dir
        dir_list = ['right', 'left', 'down', 'up']
        if SnakeList[0][0] > SnakeList[1][0]:
            dir_list.remove('left')
        if SnakeList[0][1] > SnakeList[1][1]:
            dir_list.remove('up')
        if SnakeList[0][0] < SnakeList[1][0]:
            dir_list.remove('right')
        if SnakeList[0][1] < SnakeList[1][1]:
            dir_list.remove('down')
        SnakeDir = random.choice(dir_list)
    
    return SnakeList, SnakeDir

def apple_generate(SnakeList, ApplePos):
    if len(ApplePos) == 0:
        # apple init
        x = random.randrange(1, column + 1)
        y = random.randrange(1, row + 1)
        while [x, y] in SnakeList:
            x = random.randrange(1, column + 1)
            y = random.randrange(1, row + 1)
        ApplePos = [x, y]

    return ApplePos

def update_snake(SnakeDir, SnakeList, SnakeEat, SnakeDead):
    if not SnakeDead:
        if not SnakeEat:
            SnakeList.pop(-1)
        else:
            SnakeEat = False
        
        if SnakeDir == 'up':
            SnakeList.insert(0, [SnakeList[0][0], SnakeList[0][1]-1])
        if SnakeDir == 'down':
            SnakeList.insert(0, [SnakeList[0][0], SnakeList[0][1]+1])
        if SnakeDir == 'right':
            SnakeList.insert(0, [SnakeList[0][0]+1, SnakeList[0][1]])
        if SnakeDir == 'left':
            SnakeList.insert(0, [SnakeList[0][0]-1, SnakeList[0][1]])
    return SnakeList, SnakeEat

def collision(SnakeList, ApplePos, SnakeDir, SnakeEat, SnakeDead, Score):
    # snake ate apple
    if SnakeList[0] == ApplePos:
        SnakeEat = True
        Score += 1
        ApplePos = []

    # snake and walls
    if SnakeList[0][1] == 0 and SnakeDir == 'up':
        SnakeList[0][1]=30
        #SnakeDead = True
    if SnakeList[0][1] == 31 and SnakeDir == 'down':
        SnakeList[0][1]=1
        #SnakeDead = True
    if SnakeList[0][0] == 0 and SnakeDir == 'left':
        SnakeList[0][0]=40
        #SnakeDead = True
    if SnakeList[0][0] == 41 and SnakeDir == 'right':
        SnakeList[0][0]=1
        #SnakeDead = True
    
    # snake and body
    if SnakeList[0] in SnakeList[1:]:
        SnakeDead = True
    
    return SnakeList, SnakeEat, SnakeDead, Score, ApplePos

pygame.init()
pygame.display.set_caption('Snake by Iulian Stratan')
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial_bold', 380)
running = True

while running:
    
    snake_list, snake_dir = snake_generate(snake_list, snake_dir)
    snake_list, snake_eat = update_snake(snake_dir, snake_list, snake_eat, snake_dead)
    snake_list, snake_eat, snake_dead, score, apple_pos = collision(snake_list, apple_pos, snake_dir, snake_eat, snake_dead, score)
    apple_pos = apple_generate(snake_list, apple_pos) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running == False
                break
            if event.key == pygame.K_RIGHT and not snake_list[0][0] < snake_list[1][0]:
                snake_dir = 'right'
            if event.key == pygame.K_LEFT and not snake_list[0][0] > snake_list[1][0]:
                snake_dir = 'left'
            if event.key == pygame.K_DOWN and not snake_list[0][1] < snake_list[1][1]:
                snake_dir = 'down'
            if event.key == pygame.K_UP and not snake_list[0][1] > snake_list[1][1]:
                snake_dir = 'up'
    
    # draw
    display.fill((40, 40, 40))
    
    # borders
    pygame.draw.rect(display, 'WHITE', (15, 15, 40*15, 1))
    pygame.draw.rect(display, 'WHITE', (15, 31*15, 40*15, 1))
    pygame.draw.rect(display, 'WHITE', (41*15, 15, 1, 30*15))
    pygame.draw.rect(display, 'WHITE', (15, 15, 1, 30*15))

    # score
    if snake_dead:
        img = font.render(str(score), True, (100, 30, 30))
    else:
        img = font.render(str(score), True, (60, 60, 60))
    display.blit(img, img.get_rect(center=(20*15+15, 15*15+15)).topleft)

    # apple
    if len(apple_pos) > 0:
        pygame.draw.rect(display, 'RED', (apple_pos[0]*15+1, apple_pos[1]*15+1, 13, 13))

    # snake body
    for part in snake_list[1:]:
        pygame.draw.rect(display, (220, 110, 45), (part[0]*15+1, part[1]*15+1, 13, 13))
    
    # snake head
        pygame.draw.rect(display, (215, 80, 0), (snake_list[0][0]*15+1, snake_list[0][1]*15+1, 13, 13))
    
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()