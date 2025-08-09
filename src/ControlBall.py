import numpy as np
import math
import random
from src.design import Circle
class Control:
    def is_ball_in_arc(ball_pos, circle_center, start_angle, end_angle):
        dx = ball_pos[0] - circle_center[0]
        dy = ball_pos[1] - circle_center[1]
        ball_angle = math.atan2(dy, dx)
        start_angle = start_angle % (2 * math.pi)
        end_angle = end_angle % (2 * math.pi)
        if start_angle > end_angle: 
            end_angle += 2 * math.pi
        if start_angle <= ball_angle <= end_angle or (start_angle <= ball_angle + 2 * math.pi <= end_angle):
            return True
class Ball:
    ball_pos = np.array([Circle.WIDTH /2, Circle.HEIGHT / 2 - 120], dtype = np.float64)
    ball_radius = 5
    ball_velocity = np.array([0, 0], dtype = np.float64)
    gravity = 0.5
    def __init__(self, ball_pos, ball_vel):
        self.ball_pos = np.array(ball_pos, dtype=np.float64)
        self.ball_vel = np.array(ball_vel, dtype=np.float64)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.is_in = True