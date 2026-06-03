import pygame
import random
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

G = 6.674*10e-11
class Planet:
    def __init__(self, x, y, color, mass, velocity):
        self.colorVals = color
        self.y_displacement = 0
        self.x_displacement = 0
        self.y_velocity = 0
        self.x_velocity = 0
        self.origin_x = x
        self.origin_y = y
        self.pos_x = self.origin_x
        self.pos_y = self.origin_y
        self.mass = mass
        self.collide = False
        self.perpendicularVelocity = velocity
    def update (self, dt, planets):
        
        acceleration_x = 0
        acceleration_y = 0

        for other in planets:
            if self == other: 
                continue
        
            dy = other.pos_y - self.pos_y
            dx = other.pos_x - self.pos_x
            distance = math.hypot(dy, dx) * 1000

            if distance == 0:
                continue
        
            gravitational_acceleration = (other.mass * G)/ distance ** 2
        
            acceleration_y = gravitational_acceleration * (dy/distance)
            acceleration_x = gravitational_acceleration * (dx/distance)

            # PERPENDICULAR VELOCITY

            self.x_velocity = self.perpendicularVelocity * (-dy/distance)
            self.y_velocity = self.perpendicularVelocity * (dx/distance)

            print(planets[0].pos_x, planets[0].pos_y)


        self.x_velocity += acceleration_x * dt
        self.y_velocity += acceleration_y * dt

        self.x_displacement += self.x_velocity * dt
        self.y_displacement += self.y_velocity * dt
        self.pos_x = self.origin_x + self.x_displacement
        self.pos_y = self.origin_y + self.y_displacement

    def drawPlanet(self, window):
        planet = pygame.Rect(self.pos_x, self.pos_y, 30, 30)
        pygame.draw.circle(window, (self.colorVals), planet.center, planet.width)

planet1 = Planet(3*SCREEN_WIDTH/4,SCREEN_HEIGHT/2,(25,125,250), 10e22, 200000)
planet2 = Planet(5*SCREEN_WIDTH/8,SCREEN_HEIGHT/2, (250,125,25), 4*10e22,230000)
rouge = Planet(0,SCREEN_HEIGHT/2, (125,50,50), 4*10e20,460000)
center = Planet(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, (200,125,125), 10e24, 20)

planets = [planet1, planet2, rouge, center]

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    dt = clock.tick(120)/ 500
    
    
    window.fill("black")
    for p in planets[:]:
        p.update(dt, planets)
        p.drawPlanet(window)
    pygame.display.update()