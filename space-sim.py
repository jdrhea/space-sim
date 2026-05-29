import pygame
import random

SCREEN_WIDTH = 1920/1.5
SCREEN_HEIGHT = 1080/1.5

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Planet:
    def __init__(self, x, y, x_vel, color):
        self.colorVals = color
        self.y_velocity = 0
        self.x_velocity = x_vel
        self.acceleration = 98.1
        self.pos_y = y
        self.x_displacement = 0
        self.friction = .1 #10%
        self.pos_x = x + self.x_displacement
    def update (self, dt):
        self.y_velocity += self.acceleration * dt
        self.pos_y += self.y_velocity * dt
        self.pos_x += self.x_velocity * dt

        if self.pos_y >= SCREEN_HEIGHT:
            self.y_velocity *= -1 - self.friction*-1
        if self.pos_x >= SCREEN_WIDTH or self.pos_x < 0:
            self.x_velocity *= -0.9

    def drawPlanet(self, window):
        planet = pygame.Rect(self.pos_x, self.pos_y, 30, 30)
        pygame.draw.circle(window, (self.colorVals, self.colorVals, self.colorVals), planet.center, planet.width)

planets = [Planet(random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT),100, random.randint(0,255)) for _ in range(121)]
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    dt = clock.tick(120) / 1000
    
    
    window.fill("black")
    for p in planets[:]:
        p.drawPlanet(window)
        p.update(dt)
    pygame.display.update()