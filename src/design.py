import numpy as np
import math
import pygame
class Circle:
    WIDTH = 800
    HEIGHT = 800
    circle_center = np.array([WIDTH / 2, HEIGHT / 2], dtype = np.float64)
    circle_radius = 170
class Color:
    black = (0, 0, 0)
    pink = (255, 200, 200)
    red = (255, 0, 0)
class Arc: 
    arc_degrees = 60
    start_angle = math.radians(-arc_degrees / 2)
    end_angle = math.radians(arc_degrees / 2)
    spinning_speed = 0.01
    
    def draw_arc(window, center, radius, start_angle, end_angle):
        p1 = center + (radius + 300) * np.array([math.cos(start_angle), math.sin(start_angle)])
        p2 = center + (radius + 300) * np.array([math.cos(end_angle), math.sin(end_angle)])
        pygame.draw.polygon(window, Color.black, [center, p1, p2], 0)