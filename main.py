import random
import os
import pygame

item_dic = {"rrr": 5, "melody": 10, "ggg": 14, "ggg": 10, "ggg": 30}
times = 1
characters = []
c = []
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


def gacha(item_dic, times):
    total_weight = 0
    for value in item_dic.values():
        total_weight += value

    results = []
    for i in range(times):
        results.append(lottery(item_dic, total_weight))

    return results


def lottery(item_dic, total_weight):
    score = random.randint(1, total_weight)
    range_max = 0
    for item_key, weight in item_dic.items():
        range_max += weight
        if score <= range_max:
            return item_key


item_list = gacha(item_dic, times)
f = (" ".join(item_list))
if f == 'ggg':
    image = pygame.image.load("curs.png")
    screen.blit(image, (0, 0))

if item_list not in c:
    c.append(str(item_list))
print(c)

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()