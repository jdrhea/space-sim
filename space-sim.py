import pygame
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

G = 6.674e-11
class Planet:
    def __init__(self, x, y, color, mass, velocity):
        self.colorVals = color
        self.y_displacement = 0
        self.x_displacement = 0
        self.y_grav_velocity = 0
        self.x_grav_velocity = 0
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
        self.perpendicular_x_velocity = 0
        self.perpendicular_y_velocity = 0


        for other in planets:
            if self == other: 
                continue
        
            dy = other.pos_y - self.pos_y
            dx = other.pos_x - self.pos_x
            distance = math.hypot(dy, dx) * 1000

            if distance == 0:
                continue
        
            gravitational_acceleration = (other.mass * G) / distance ** 2

            # accumulate accelerations from all other bodies
            acceleration_y += gravitational_acceleration * (dy / distance)
            acceleration_x += gravitational_acceleration * (dx / distance)

            # accumulate perpendicular (tangential) velocity components
            self.perpendicular_x_velocity += self.perpendicularVelocity * (-dy / distance)
            self.perpendicular_y_velocity += self.perpendicularVelocity * (dx / distance)


        self.x_grav_velocity += acceleration_x * dt
        self.y_grav_velocity += acceleration_y * dt

        self.x_velocity = self.x_grav_velocity + self.perpendicular_x_velocity
        self.y_velocity = self.y_grav_velocity + self.perpendicular_y_velocity

        self.x_displacement += self.x_velocity * dt
        self.y_displacement += self.y_velocity * dt


        self.pos_x = self.origin_x + self.x_displacement
        self.pos_y = self.origin_y + self.y_displacement


    def drawPlanet(self, window):
        planet = pygame.Rect(self.pos_x, self.pos_y, 30, 30)
        radius = planet.width // 2
        pygame.draw.circle(window, (self.colorVals), planet.center, radius)

planet1 = Planet(7*SCREEN_WIDTH/8,SCREEN_HEIGHT/2,(25,125,250), 1e23, 0)
planet2 = Planet(5*SCREEN_WIDTH/8,SCREEN_HEIGHT/2, (250,125,25), 1e22,10000)
center = Planet(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, (200,125,125), 5e0, 1000)

planets = [planet1, center]

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    dt = clock.tick(120) / 100
    
    
    window.fill("black")
    for p in planets[:]:
        p.update(dt, planets)
        p.drawPlanet(window)
    pygame.display.update()