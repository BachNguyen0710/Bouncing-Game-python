import pygame
import numpy as np
import math
import random
from src.design import Circle, Color, Arc
from src.ControlBall import Control, Ball

pygame.init()
pygame.display.set_caption("Bouncing Ball")
window = pygame.display.set_mode((Circle.WIDTH, Circle.HEIGHT))
clock = pygame.time.Clock()
running = True
is_ball_in = True
balls = [Ball(Ball.ball_pos, Ball.ball_velocity)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(Color.black)
    Arc.start_angle += Arc.spinning_speed
    Arc.end_angle += Arc.spinning_speed
    for ball in balls:
        ball.ball_vel[1] += Ball.gravity 
        ball.ball_pos[0] += ball.ball_vel[0]
        ball.ball_pos[1] += ball.ball_vel[1]
        if ball.ball_pos[1] > Circle.HEIGHT or ball.ball_pos[0] < 0 or ball.ball_pos[0] > Circle.WIDTH or ball.ball_pos[1] < 0: 
            balls.remove(ball)
            balls.append(Ball([Circle.WIDTH // 2, Circle.HEIGHT // 2 - 120], [random.uniform(-4, 4), random.uniform(-1, 1)]))
            balls.append(Ball([Circle.WIDTH // 2, Circle.HEIGHT // 2 - 120], [random.uniform(-4, 4), random.uniform(-1, 1)]))
        dist = np.linalg.norm(ball.ball_pos - Circle.circle_center)
        if dist + Ball.ball_radius > Circle.circle_radius:
            if Control.is_ball_in_arc(ball.ball_pos, Circle.circle_center, Arc.start_angle, Arc.end_angle):
                ball.is_in = False
            if ball.is_in:
                normal = (ball.ball_pos - Circle.circle_center) / dist
                d = ball.ball_pos - Circle.circle_center
                t = np.array([-d[1], d[0]], dtype = np.float64)
                ball.ball_vel = ball.ball_vel - 2 * np.dot(ball.ball_vel, normal) * normal
                ball.ball_pos = Circle.circle_center + (Circle.circle_radius - Ball.ball_radius) * normal
                ball.ball_vel[1] *= 0.9
                ball.ball_vel += t*Arc.spinning_speed
    pygame.draw.circle(window, Color.pink, Circle.circle_center, Circle.circle_radius, 3)
    Arc.draw_arc(window, Circle.circle_center, Circle.circle_radius, Arc.start_angle, Arc.end_angle)
    for ball in balls:
        pygame.draw.circle(window, ball.color, ball.ball_pos, Ball.ball_radius)
    pygame.display.update() 
    clock.tick(60)
pygame.quit()
