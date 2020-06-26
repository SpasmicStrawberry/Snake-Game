import pygame
import random

screenWidth = 500
screenLength = 800

clock = pygame.time.Clock()

class Snake:
    def __init__(self,x,y):
        self.speed = 5
        self.direction = "down"
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

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getSize(self):
        return self.size

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.size,self.size])

class Snack:
    def __init__(self):
        self.size = 5
        self.color = [255,255,255]
        self.x = 5*(random.randint(0,160))
        self.y = 5*(random.randint(0,120))

    def changePos(self):
        self.x = 5*(random.randint(0,160))
        self.y = 5*(random.randint(0,120))

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getSize(self):
        return self.size

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,[self.x,self.y],self.size)

def eatSnack(snakeX,snakeY,snackX,snackY,snakeSize,snackSize):
    if (snackY > snakeY) and (snackY + snackSize < snakeY + snakeSize) and\
        (snackX < snakeX + snakeSize):
        return True
    return False

def main():
    screen = pygame.display.set_mode([screenLength,screenWidth])
    startX = 400
    starty = 300

    snake = Snake(startX,starty)
    snack = Snack()

    crashed = False
    while not crashed:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            crashed = True
        
        clock.tick(60)
        screen.fill([0,0,0])

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP:
                direction = "up"
            if ev.key == pygame.K_DOWN:
                direction = "down"
            if ev.key == pygame.K_LEFT:
                direction = "left"
            if ev.key == pygame.K_RIGHT:
                direction = "right"
            snake.setDirection(direction)

        snake.move()
        snake.draw(screen)
        snack.draw(screen)
        pygame.display.flip()
main()