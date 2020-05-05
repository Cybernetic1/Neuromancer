# -*- coding: utf8 -*-

import numpy
import math

N = 2

def set_distance(x1, x2):
	Σ, Σ1, Σ2 = 0.0, 0.0, 0.0

	for i in range(N):
		for j in range(N):
			Σ += (x1[i] - x2[j]) **2

	for i in range(N):
		for j in range(N):
			Σ1 += (x1[i] - x1[j]) **2

	for i in range(N):
		for j in range(N):
			Σ2 += (x2[i] - x2[j]) **2

	dx = (2 * numpy.sqrt(Σ / N) - numpy.sqrt(Σ1 / N) - numpy.sqrt(Σ2 / N)) / 2
	return dx

import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0xff,0xff,0xff))

R = 50
for x in range(0, 1050, 50):
	for y in range(0, 1050, 50):
		if x >= y:
			D = int(21 - (x/50 - y/50))
			print(D)
			for n in range(0, 800):
				θ = 2 * math.pi * n / 800
				x1 = (x + R * math.cos(θ))
				y1 = (y + R * math.sin(θ))

				d = set_distance([x,y], [x1,y1]) * 2
				x2 = int(x + d * math.cos(θ))
				y2 = int(y + d * math.sin(θ))

				if (x/50 - y/50) % 2 == 1:
					color = (0xff, 0x00, 0x00)
				else:
					color = (0x00, 0x00, 0xff)
				screen.set_at((x2, 1000-y2), color)
				# pygame.draw.circle(screen, (0x00,0x77,0x77), [x,1000-y], 5)

pygame.draw.line(screen, (0x00,0xff,0x00), [0,1000], [1000,0], 2)
pygame.display.flip()

input("Pause...")
exit(0)

