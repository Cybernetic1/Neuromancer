# -*- coding: utf8 -*-

import numpy
import math

N = 2

def self_distance(x):
	Σ = 0.0
	for i in range(N):
		for j in range(N):
			Σ += (x[i] - x[j]) **2
	d_self = numpy.sqrt(Σ / N)
	return d_self

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

	dx = 10 * numpy.sqrt(Σ / N) / (1 + (numpy.sqrt(Σ1 / N) + numpy.sqrt(Σ2 / N)) / 2)
	return dx

def Euclidean_distance(x1, x2):
	Σ = 0.0

	for i in range(N):
		Σ += (x1[i] - x2[i]) **2

	dx = numpy.sqrt(Σ / N)
	return dx

def set_distance0(x1, x2):
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

# This distance metric is pathological, used only for testing purposes:
def set_distance2(x1, x2):
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

	dx = numpy.sqrt((2 * Σ - Σ1 - Σ2) / N / 2)
	return dx

import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0xff,0xff,0xff))
pygame.draw.line(screen, (0x00,0xff,0x00), [0,1000], [1000,0], 2)

R = 100
x_divs = 100
y_divs = 100
for x in range(0, 1000 + x_divs, x_divs):
	for y in range(0, 1000 + y_divs, y_divs):
		if x >= y:
			D = int(21 - (x/x_divs - y/y_divs))
			print(D)
			for n in range(0, 800):
				θ = 2 * math.pi * n / 800
				x1 = (x + R * math.cos(θ))
				y1 = (y + R * math.sin(θ))

				# print(x, y, x1, y1)
				d = Euclidean_distance([x,y], [x1,y1]) * 1
				x2 = int(x + d * math.cos(θ))
				y2 = int(y + d * math.sin(θ))

				pygame.draw.circle(screen, (0x00,0xff,0x00), [x,1000-y], 3)

				# d_self = self_distance([x, y]) * 0.5
				# pygame.draw.line(screen, (0xaa,0xaa,0xaa), [x,1000-y], [x - 50,1000-y - d_self], 2)

				if (x/x_divs - y/y_divs) % 2 == 1:
					color = (0xff, 0x00, 0x00)
				else:
					color = (0x00, 0x00, 0xff)
				screen.set_at((x2, 1000-y2), color)

pygame.display.flip()

input("Pause...")
exit(0)
