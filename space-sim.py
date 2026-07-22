import pygame
import math
import random

SCREEN_WIDTH = 1920/1.5
SCREEN_HEIGHT = 1080/1.5

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('Gill Sans', 48)
G = 6.674e-11
METERS_CONVERSION = 1e6
playback_speed = 100
class Planet:
    def __init__(self, x, y, color, mass, velocity, density):
        self.colorVals = color
        self.y_velocity = velocity
        self.x_velocity = 0
        self.pos_x = x * METERS_CONVERSION
        self.pos_y = y * METERS_CONVERSION
        self.mass = mass
        self.collide = False
        self.perpendicularVelocity = velocity
        self.volume = mass/density
        self.radius = math.cbrt(.75*self.volume/math.pi) / 1e6
        self.distance_to_center = 0
        self.gravitational_acceleration = 0
        self.orbital_velocity = 0
        self.orbitalEccentricity = 0

    def setInitialVelocity(self):
        dx = center.pos_x - self.pos_x
        dy = center.pos_y - self.pos_y

        distance = math.hypot(dx, dy)

        if distance == 0:
            return

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

            dx = center.pos_x - self.pos_x
            dy = center.pos_y - self.pos_y

            self.distance_to_center = math.hypot(dx, dy)

            if distance == 0:
                continue
            if self.distance_to_center == 0:
                continue
        
            self.gravitational_acceleration = (other.mass * G) / distance ** 2

            # accumulate accelerations from all other bodies
            acceleration_y += self.gravitational_acceleration * (dy / distance)
            acceleration_x += self.gravitational_acceleration * (dx / distance)

            self.orbital_velocity = math.sqrt((G*1e30)/(abs(self.distance_to_center)))
            self.orbitalEccentricity =  1-abs((self.perpendicularVelocity/self.orbital_velocity)**2 - 1)


        self.x_velocity += acceleration_x * dt
        self.y_velocity += acceleration_y * dt

        self.pos_x += self.x_velocity * dt
        self.pos_y += self.y_velocity * dt


    def drawPlanet(self, window):
        screen_x = self.pos_x / METERS_CONVERSION
        screen_y = self.pos_y / METERS_CONVERSION

        self.planetRect = pygame.Rect(screen_x,screen_y, self.radius*2, self.radius*2)
        self.clickableRect = pygame.Rect(screen_x - self.planetRect.width * 2, screen_y - self.planetRect.height * 2, self.planetRect.width *4, self.planetRect.height *4)
        radius = self.planetRect.width // 2
        pygame.draw.circle(window, (self.colorVals), (self.planetRect.centerx - radius,self.planetRect.centery - radius), 2*radius)

center = Planet(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, (200,125,125), 1e30, 0,10000000)
planet1 = Planet(6*SCREEN_WIDTH/8,SCREEN_HEIGHT/2,(25,125,250), 1e24, math.sqrt((G*center.mass)/((SCREEN_WIDTH/4)*METERS_CONVERSION)),5000)
planet2 = Planet(5*SCREEN_WIDTH/8,SCREEN_HEIGHT/2, (250,125,25), 1e22, math.sqrt((G*center.mass)/((SCREEN_WIDTH/8)*METERS_CONVERSION)),30)
planet3 = Planet(6.5*SCREEN_WIDTH/8,SCREEN_HEIGHT/2, (25,200,125), 1e23, math.sqrt((G*center.mass)/((2.5*SCREEN_WIDTH/8)*METERS_CONVERSION)),30)
planet4 = Planet(7.5*SCREEN_WIDTH/8,SCREEN_HEIGHT/2, (200,200,125), 1e25, math.sqrt((G*center.mass)/((3.5*SCREEN_WIDTH/8)*METERS_CONVERSION)),3000)
rougeStar = Planet(SCREEN_WIDTH,SCREEN_HEIGHT, (200,200,0), 5e29, 100,3000000)

planets = [center,planet1,planet2,planet3,planet4]
XposText = font.render("", True, 'white')
YposText = font.render("", True, 'white')
orbitalDistance = font.render("", True, 'white')
radiusText = font.render("", True, 'white')
massText = font.render("", True, 'white')

initialVelocityText = font.render("", True, 'white')
x_VelocityText = font.render("", True, 'white')
y_VelocityText = font.render("", True, 'white')
accelerationText = font.render("", True, 'white')

OEIText = font.render("", True, 'white')




for p in planets:
    if p != center:
        p.setInitialVelocity()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3: 
                x_pos,y_pos = event.pos
                new_planet = Planet(x_pos,y_pos, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1e22, math.sqrt((G*1e30)/(abs(x_pos - SCREEN_WIDTH/2)*1e6)),50)
                new_planet.setInitialVelocity()
                planets.append(new_planet)
    

    raw_dt = clock.tick(60) / 1000
    dt = playback_speed * raw_dt

    
    window.fill("black")
    for p in planets[:]:
        p.update(dt, planets)
        p.drawPlanet(window)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if p.clickableRect.collidepoint(event.pos):
                    XposText = font.render("X: " + str(round(p.pos_x/METERS_CONVERSION)) + "Mm", True, 'white')
                    YposText = font.render("Y: " + str(round(p.pos_y/METERS_CONVERSION)) + "Mm", True, 'white')
                    orbitalDistance = font.render("Orbital Dist: " + str(round(p.distance_to_center/METERS_CONVERSION)) + "Mm", True, 'white')
                    radiusText = font.render("Radius: " + str(p.radius * 1e3) + " km", True, 'white')
                    massText = font.render("Mass: " + str(p.mass) + " kg", True, 'white')
                    initialVelocityText = font.render("Initial Velocity: " + str(round(p.perpendicularVelocity/ 1e3)) + " km/s", True, 'white')
                    x_VelocityText = font.render("X_Velocity: " + str(round(p.x_velocity/ 1e3)) + " km/s", True, 'white')
                    y_VelocityText = font.render("Y_Velocity: " + str(round(p.y_velocity/1e3)) + " km/s", True, 'white')
                    accelerationText = font.render("Accel: " + str(p.gravitational_acceleration) + "m/s^2", True, 'white')
                    OEIText = font.render("C.O.I: " + str(p.orbitalEccentricity), True, 'white')
    window.blit(XposText, (SCREEN_WIDTH - SCREEN_WIDTH/3,SCREEN_HEIGHT / 16))
    window.blit(YposText, (SCREEN_WIDTH - SCREEN_WIDTH/3,SCREEN_HEIGHT / 8))
    window.blit(orbitalDistance, (SCREEN_WIDTH - SCREEN_WIDTH/3,3*SCREEN_HEIGHT / 16))
    window.blit(radiusText, (SCREEN_WIDTH - SCREEN_WIDTH/3,SCREEN_HEIGHT / 4))
    window.blit(massText, (SCREEN_WIDTH - SCREEN_WIDTH/3,5*SCREEN_HEIGHT / 16))
    window.blit(initialVelocityText, (SCREEN_WIDTH - SCREEN_WIDTH/3,7*SCREEN_HEIGHT / 16))
    window.blit(x_VelocityText, (SCREEN_WIDTH - SCREEN_WIDTH/3,SCREEN_HEIGHT / 2))
    window.blit(y_VelocityText, (SCREEN_WIDTH - SCREEN_WIDTH/3,9*SCREEN_HEIGHT / 16))
    window.blit(OEIText, (SCREEN_WIDTH - SCREEN_WIDTH/3,11*SCREEN_HEIGHT / 16))
    window.blit(accelerationText, (SCREEN_WIDTH - SCREEN_WIDTH/3,3*SCREEN_HEIGHT / 4))
    pygame.display.flip()