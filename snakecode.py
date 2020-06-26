import pygame

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
        self.size = 10
    
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

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.size,self.size])

def main():
    screen = pygame.display.set_mode([screenLength,screenWidth])
    startX = 400
    starty = 300

    snake = Snake(startX,starty)

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
        pygame.display.flip()
main()
