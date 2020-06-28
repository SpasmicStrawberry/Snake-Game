import pygame
import random

screenWidth = 600
screenLength = 800

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
        self.y = self.size*(random.randint(0,screenWidth/self.size-1))

    def changePos(self):
        self.x = self.size*(random.randint(0,screenLength/self.size-1))
        self.y = self.size*(random.randint(0,screenWidth/self.size-1))

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
    if y < 0 or y >= screenWidth:
        return True
    return False

#checks if the snake hit itself
def hitSelf(x,y,snake):
    for i in range(5,len(snake)):
        if snake[i].getX() == x and snake[i].getY() == y:
            return True
    return False

#main game function
def main():
    screen = pygame.display.set_mode([screenLength,screenWidth])
    startX = 400
    starty = 300
    direction = "down"

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
            if ev.key == pygame.K_DOWN and snake[0].getDirection() != "up":
                direction = "down"
            if ev.key == pygame.K_LEFT and snake[0].getDirection() != "right":
                direction = "left"
            if ev.key == pygame.K_RIGHT and snake[0].getDirection() != "left":
                direction = "right"
            snake[0].setDirection(direction)

        #food has been eaten
        if eatfood(snake[0].getX(),snake[0].getY(),food.getX(),food.getY()):
            side = snake[len(snake)-1].getDirection()
            if side == "up":
                direction = "up"
                x = snake[len(snake)-1].getX()
                y = snake[len(snake)-1].getY() + snake[0].getSize()
            elif side == "down":
                direction = "down"
                x = snake[len(snake)-1].getX()
                y = snake[len(snake)-1].getY() - snake[0].getSize()
            elif side == "left":
                direction = "left"
                x = snake[len(snake)-1].getX() + snake[0].getSize()
                y = snake[len(snake)-1].getY()
            else:
                direction = "right"
                x = snake[len(snake)-1].getX() - snake[0].getSize()
                y = snake[len(snake)-1].getY()
            snake.append(Snake(x,y,direction))
            food.changePos()

        #update snake
        snake[0].move()
        snake[0].draw(screen)
        for i in range(1,len(snake)):
            tempDir = snake[i].getDirection()
            snake[i].setDirection(direct)
            snake[i].move()
            snake[i].draw(screen)
            direct = tempDir

        if outOfBounds(snake[0].getX(),snake[0].getY()) or \
            hitSelf(snake[0].getX(),snake[0].getY(),snake):
            crashed = True

        food.draw(screen)
        pygame.display.flip()

        pygame.time.delay(80)
main()