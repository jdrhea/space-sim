import pygame
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

G = 6.674e-11
playback_speed = 1
class Planet:
    def __init__(self, x, y, color, mass, velocity):
        self.colorVals = color
        self.y_displacement = 0
        self.x_displacement = 0
        self.y_velocity = velocity
        self.x_velocity = 0
        self.origin_x = x
        self.origin_y = y
        self.pos_x = self.origin_x
        self.pos_y = self.origin_y
        self.mass = mass
        self.collide = False
        self.perpendicularVelocity = velocity

    def setInitialVelocity(self, planets):
        for other in planets:
            if self == other: 
                continue
            dx = center.pos_x - self.pos_x
            dy = center.pos_y - self.pos_y

            distance = math.hypot(dx, dy)

            if distance == 0:
                continue

            self.x_velocity = self.perpendicularVelocity * (-dy / distance)
            self.y_velocity = self.perpendicularVelocity * (dx / distance)

    def update (self, dt, planets):
        
        acceleration_x = 0
        acceleration_y = 0

        for other in planets:
            if self == other: 
                continue
        
            dy = other.pos_y - self.pos_y
            dx = other.pos_x - self.pos_x
            distance = math.hypot(dy, dx)

            if distance == 0:
                continue

            METERS_CONVERSION = 1e6

            dx_meters = dx * METERS_CONVERSION
            dy_meters = dy * METERS_CONVERSION

            distance_meters = math.hypot(dx_meters, dy_meters)
        
            gravitational_acceleration = (other.mass * G) / distance_meters ** 2

            # accumulate accelerations from all other bodies
            acceleration_y += gravitational_acceleration * (dy_meters / distance_meters)
            acceleration_x += gravitational_acceleration * (dx_meters / distance_meters)
            print(math.sqrt((G*1e30)/((SCREEN_WIDTH/4)*1e6))/1000000)


        self.x_velocity += acceleration_x * dt
        self.y_velocity += acceleration_y * dt

        self.x_displacement += self.x_velocity * dt
        self.y_displacement += self.y_velocity * dt


        self.pos_x = self.origin_x + self.x_displacement
        self.pos_y = self.origin_y + self.y_displacement
    def drawPlanet(self, window):
        planet = pygame.Rect(self.pos_x, self.pos_y, 30, 30)
        radius = planet.width // 2
        pygame.draw.circle(window, (self.colorVals), planet.center, 2*radius)

center = Planet(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, (200,125,125), 1e30, 0)
planet1 = Planet(6*SCREEN_WIDTH/8,SCREEN_HEIGHT/2,(25,125,250), 1e24, math.sqrt((G*1e30)/((SCREEN_WIDTH/4)*1e6))/1000)
planet2 = Planet(5*SCREEN_WIDTH/8,SCREEN_HEIGHT/2, (250,125,25), 1e22, math.sqrt((G*1e30)/((SCREEN_WIDTH/8)*1e6))/1000)

planets = [planet1,planet2, center]

for p in planets:
    p.setInitialVelocity(planets)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    raw_dt = clock.tick(120) / 1000
    dt = playback_speed * raw_dt
    
    
    window.fill("black")
    for p in planets[:]:
        p.update(dt, planets)
        p.drawPlanet(window)
    pygame.display.update()