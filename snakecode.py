import pygame
import random

screenWidth = 600
screenLength = 800

clock = pygame.time.Clock()

class Snake:
    def __init__(self,x,y):
        self.speed = 5
        self.direction = "down"
        self.x = x
        self.y = y
        self.color = [0,0,255]
        self.size = 25
    
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
        self.size = 5
        self.color = [255,255,255]
        self.x = 5*(random.randint(2,158))
        self.y = 5*(random.randint(2,118))

    def changePos(self):
        self.x = 5*(random.randint(2,158))
        self.y = 5*(random.randint(2,118))

    def getSize(self):
        return self.size

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,[self.x,self.y],self.size)

def eatfood(snakeX,snakeY,foodX,foodY,snakeSize,foodSize):
    if (foodY > snakeY - foodSize) and \
        (foodY < snakeY + snakeSize + foodSize) and\
        (foodX > snakeX - foodSize) and \
        (foodX < snakeX + snakeSize + foodSize):
        return True
    return False

def main():
    screen = pygame.display.set_mode([screenLength,screenWidth])
    startX = 400
    starty = 300
    direction = "down"

    snake = []
    snake.append(Snake(startX,starty))
    food = Food()

    crashed = False
    while not crashed:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            crashed = True
        
        clock.tick(60)
        screen.fill([0,0,0])

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP and snake[0].getDirection() != "down":
                direction = "up"
            if ev.key == pygame.K_DOWN and snake[0].getDirection() != "up":
                direction = "down"
            if ev.key == pygame.K_LEFT and snake[0].getDirection() != "right":
                direction = "left"
            if ev.key == pygame.K_RIGHT and snake[0].getDirection() != "left":
                direction = "right"
            snake[0].setDirection(direction)

        if eatfood(snake[0].getX(),snake[0].getY(),food.getX(),\
            food.getY(),snake[0].getSize(),food.getSize()):
            food.changePos()

        snake[0].move()
        snake[0].draw(screen)
        food.draw(screen)
        pygame.display.flip()
main()