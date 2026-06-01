import pygame
import random
import math

SCREEN_WIDTH = 1920/1.5
SCREEN_HEIGHT = 1080/1.5

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

G = 6.674*10e-11
class Planet:
    def __init__(self, x, y, color, mass):
        self.colorVals = color
        self.y_velocity = 0
        self.x_velocity = 0
        self.y_displacement = 0
        self.x_displacement = 0
        self.origin_x = x
        self.origin_y = y
        self.pos_x = self.origin_x
        self.pos_y = self.origin_y
        self.mass = mass
        self.collide = False
    def update (self, dt, planets):
        # self.y_velocity += self.acceleration * dt
        # self.pos_y += self.y_velocity * dt
        # self.pos_x += self.x_velocity * dt
        acceleration_x = 0
        acceleration_y = 0

        for other in planets:
            if self == other: 
                continue
        
            dy = other.pos_y - self.pos_y
            dx = other.pos_x - self.pos_x
            distance = math.hypot(dy, dx) * 500

            if distance == 0:
                continue
        
            gravitational_acceleration = (other.mass * G)/ distance ** 2
        
            acceleration_y = gravitational_acceleration * (dy/distance)
            acceleration_x = gravitational_acceleration * (dx/distance)


        self.x_velocity += acceleration_x * dt
        self.y_velocity += acceleration_y * dt

        self.x_displacement += self.x_velocity * dt
        self.y_displacement += self.y_velocity * dt
        self.pos_x = self.origin_x + self.x_displacement
        self.pos_y = self.origin_y + self.y_displacement

        if abs(distance <= 5000):
            self.collide = True
        if self.collide == True:
            acceleration_x *= 0.001
            acceleration_y *= 0.001


        print(planets[1].collide, planets[2].collide)


    def drawPlanet(self, window):
        planet = pygame.Rect(self.pos_x, self.pos_y, 30, 30)
        pygame.draw.circle(window, (self.colorVals), planet.center, planet.width)

planet1 = Planet(0,SCREEN_HEIGHT/2,(25,125,250), 2*10e22)
planet2 = Planet(SCREEN_WIDTH,SCREEN_HEIGHT/2, (250,125,25), 4*10e22)
planet3 = Planet(SCREEN_WIDTH/2,0, (200,125,125), 10e23)

planets = [planet1, planet2, planet3]

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    dt = clock.tick(120) / 1000
    
    
    window.fill("black")
    for p in planets[:]:
        p.update(dt, planets)
        p.drawPlanet(window)
    # for p in planets[:]:
    #     if p.planet.colliderect(p.rect):
    #         p.x_velocity *= -1
    #         p.y_velocity *= -1
    pygame.display.update()