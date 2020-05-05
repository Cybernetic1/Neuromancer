# -*- coding: utf8 -*-

import math
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0xff,0xff,0xff))

r = 50
for x in range(0, 1050, 50):
	for y in range(0, 1050, 50):
		if x >= y:
			for n in range(0, 72):
				θ = 2 * math.pi * n / 72
				x1 = int(x + r * math.cos(θ))
				y1 = int(1000-y + r * math.sin(θ))
				screen.set_at((x1, y1), (0x77,0x00,0x77))
				# pygame.draw.circle(screen, (0x00,0x77,0x77), [x,1000-y], 5)

pygame.draw.line(screen, (0x00,0x77,0x77), [0,1000], [1000,0], 2)
pygame.display.flip()

input("Pause...")
exit(0)

H = 1000
h = float(H) - 3.0
x = 1.0
dx = 999.0 / len(pop)
# dn = int(math.ceil(dx))
dn = int(dx)
# ymax = max(pop, key = lambda x: x['fitness'])['fitness']
# print("ymax =", ymax)
ymax = 20.0
pygame.draw.line(screen, (0xFF,0x77,0x77), [int(x),H], [int(x),H+int(z*1.0)], dn)

