import pygame
pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
blue = (0,0,255)
red = (255,0,0)
pygame.display.update()

class Circle():
    def __init__(self, color, pos, radius, width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = screen

    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

rcircle = Circle(red,(300,300),25,0)
bcircle = Circle(blue,(300,300),35,0)
rcircle.draw()
bcircle.draw()