import pygame
import random

pygame.init()
screenWidth = 660
screenLength = 800
font = pygame.font.SysFont("calibri", 32)

clock = pygame.time.Clock()

class Snake:
    def __init__(self,x,y,direction):
        self.speed = 20
        self.direction = direction
        self.x = x
        self.y = y
        self.color = [0,0,255]
        self.size = 20
    
    def move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed

    def setDirection(self,direction):
        self.direction = direction

    def getDirection(self):
        return self.direction

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getSize(self):
        return self.size

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.size,self.size])

class Food:
    def __init__(self):
        self.size = 20
        self.color = [255,255,255]
        self.x = self.size*(random.randint(0,screenLength/self.size-1))
        self.y = self.size*(random.randint(3,screenWidth/self.size-1))

    def changePos(self):
        self.x = self.size*(random.randint(0,screenLength/self.size-1))
        self.y = self.size*(random.randint(3,screenWidth/self.size-1))

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.size,self.size])

#checks if the snake touched the food
def eatfood(snakeX,snakeY,foodX,foodY):
    if snakeX == foodX and snakeY == foodY:
        return True
    return False

#checks if the snake is out of bounds
def outOfBounds(x,y):
    if x < 0 or x >= screenLength:
        return True
    if y < 60 or y >= screenWidth:
        return True
    return False

#checks if the snake hit itself
def hitSelf(x,y,snake):
    for i in range(5,len(snake)):
        if snake[i].getX() == x and snake[i].getY() == y:
            return True
    return False

#displays the score 
def drawScoreBoard(screen,points):
    color = [255,255,255]
    pygame.draw.rect(screen,color,[0,0,800,60])
    score = font.render("Score: " + str(points), True, (0,0,0))
    screen.blit(score, (20,0))

#main game function
def main():
    points = 0
    screen = pygame.display.set_mode([screenLength,screenWidth])
    startX = 400
    starty = 300
    direction = "right"

    snake = []
    snake.append(Snake(startX,starty,direction))
    food = Food()

    crashed = False
    while not crashed:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            crashed = True
        
        clock.tick(60)
        screen.fill([0,0,0]) 
        
        #controling the snake
        direct = snake[0].getDirection() #this will be used to update the 2nd snake
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP and snake[0].getDirection() != "down":
                direction = "up"
            elif ev.key == pygame.K_DOWN and snake[0].getDirection() != "up":
                direction = "down"
            elif ev.key == pygame.K_LEFT and snake[0].getDirection() != "right":
                direction = "left"
            elif ev.key == pygame.K_RIGHT and snake[0].getDirection() != "left":
                direction = "right"
            snake[0].setDirection(direction)

        #update snake
        snake[0].move()

        #lose conditions
        if outOfBounds(snake[0].getX(),snake[0].getY()) or \
            hitSelf(snake[0].getX(),snake[0].getY(),snake):
            crashed = True
            break
        
        #redraw the snake
        snake[0].draw(screen)
        for i in range(1,len(snake)):
            tempDir = snake[i].getDirection()
            snake[i].setDirection(direct)
            snake[i].move()
            snake[i].draw(screen)
            direct = tempDir

        #food has been eaten
        if eatfood(snake[0].getX(),snake[0].getY(),food.getX(),food.getY()):
            points+=1
            side = snake[len(snake)-1].getDirection()
            if side == "up":
                x = snake[len(snake)-1].getX()
                y = snake[len(snake)-1].getY() + snake[0].getSize()
            elif side == "down":
                x = snake[len(snake)-1].getX()
                y = snake[len(snake)-1].getY() - snake[0].getSize()
            elif side == "left":
                x = snake[len(snake)-1].getX() + snake[0].getSize()
                y = snake[len(snake)-1].getY()
            else:
                x = snake[len(snake)-1].getX() - snake[0].getSize()
                y = snake[len(snake)-1].getY()
            snake.append(Snake(x,y,side))
            food.changePos()
            while any(e.getX() == food.getX() for e in snake) and\
                any(e.getY() == food.getY() for e in snake):
                food.changePos()
        #redraw food
        food.draw(screen)

        #update score board
        drawScoreBoard(screen,points)
        
        pygame.display.flip()

        #controls the speed of the snake
        pygame.time.delay(80)
    
    #death animation
    while len(snake) > 0:
        clock.tick(60)
        screen.fill([0,0,0])
        snake.pop(0)

        for e in snake:
            e.draw(screen)

        drawScoreBoard(screen,points)
        pygame.display.flip()
        pygame.time.delay(100)

main()