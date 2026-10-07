import pygame
import math
from datetime import datetime
import random

height = 640
width = 480
radius = 200

start = (height/2, width/2)
length = width/3
angle = 0
angle_offset = 360/12
screen = pygame.display.set_mode((height,width))

for line_counter in range(12):
    angle = line_counter * angle_offset
    x_offset = math.cos(math.radians(angle))*length
    y_offset = math.sin(math.radians(angle))*length
    end = (start[0] + x_offset, start[1] + y_offset)
    pygame.draw.line(screen, (236, 95, 128), start, end, width=5)

#overtegner første del af de lyserøde streger
start = (height/2, width/2)
length = width/3
angle = 0
angle_offset = 360/12

for line_counter in range(12):
    angle = line_counter * angle_offset
    x_offset = math.cos(math.radians(angle))*length
    y_offset = math.sin(math.radians(angle))*length
    end = (start[0] + x_offset, start[1] + y_offset)
    pygame.draw.line(screen, (255, 255, 255), start, end, width=7)

now = datetime.now()
seconds = now.second
minutes = now.minute
hours = now.hour
clock = pygame.time.Clock()

viser_start_point = (height/2, width/2)
viser_length_sekund = 165
viser_length_minute = 140
viser_length_timer = 120



pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    time= datetime.now()
    now = datetime.now()
    seconds = now.second
    minutes = now.minute
    hours = now.hour
    clock = pygame.time.Clock()

    #laver skærmen
    pygame.init()
    screen = pygame.display.set_mode((height,width))
    screen.fill((255, 255, 255))

    #tegner cirklen
    pygame.draw.circle(screen,(110,210,83),(height/2,width/2),radius,width=3)

#tegner 1-12 punkterne
    start = (height/2, width/2)
    length = radius
    angle = 0
    angle_offset = 360/12

    for line_counter in range(12):
        angle = line_counter * angle_offset
        x_offset = math.cos(math.radians(angle))*length
        y_offset = math.sin(math.radians(angle))*length
        end = (start[0] + x_offset, start[1] + y_offset)
        pygame.draw.line(screen, (236, 95, 128), start, end, width=5)

#overtegner første del af de lyserøde streger
    start = (height/2, width/2)
    length = width/3
    angle = 0
    angle_offset = 360/12

    for line_counter in range(12):
        angle = line_counter * angle_offset
        x_offset = math.cos(math.radians(angle))*length
        y_offset = math.sin(math.radians(angle))*length
        end = (start[0] + x_offset, start[1] + y_offset)
        pygame.draw.line(screen, (255, 255, 255), start, end, width=7)

    #visere
    grad_sek = seconds * 6 -90
    x = viser_start_point[0] + viser_length_sekund * math.cos(math.radians(grad_sek))
    y = viser_start_point[1] + viser_length_sekund * math.sin(math.radians(grad_sek))
    pygame.draw.line(screen, (0,0,0), viser_start_point, (x,y), 2)

    grad_min = minutes* 6 -90
    x = viser_start_point[0] + viser_length_minute * math.cos(math.radians(grad_min))
    y = viser_start_point[1] + viser_length_minute * math.sin(math.radians(grad_min))
    pygame.draw.line(screen, (0,0,0), viser_start_point, (x,y), 4)

    grad_timer =((hours % 12) * 30) + (minutes * 0.5) -90
    x = viser_start_point[0] + viser_length_timer * math.cos(math.radians(grad_timer))
    y = viser_start_point[1] + viser_length_timer * math.sin(math.radians(grad_timer))
    pygame.draw.line(screen, (0,0,0), viser_start_point, (x,y), 6)


    pygame.display.flip()
    clock.tick(60)
