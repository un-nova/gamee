import random
import os
import pygame

item_dic = {" keroppi": 5, "hello kitty": 10, "my melody": 14, "cinnamoroll": 10, "kuromi": 30}
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


pygame.display.set_caption('HelloKitty Garden')


def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[1::-1]
    format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
    cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()


def loadGIF(filename):
    gif = cv2.VideoCapture(filename)
    frames = []
    while True:
        ret, cv2Image = gif.read()
        if not ret:
            break
        pygameImage = cv2ImageToSurface(cv2Image)
        frames.append(pygameImage)
    return frames


pygame.init()
window = pygame.display.set_mode((650, 500))
clock = pygame.time.Clock()

gifFrameList = loadGIF(r"pix.gif")
currentFrame = 0

run = True
while run:
    clock.tick(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos >= (250, 0):
                    if mopos <= (450, 0):
                        clock = pygame.time.Clock()
                        autog = 0
                        coins = 0
                        display_width = 650
                        display_height = 500
                        white = (255, 255, 255)
                        black = (0, 0, 0)
                        grey = (128, 128, 128)
                        light_grey = (224, 224, 224)
                        light_blue = (173, 216, 230)
                        grey = (128, 128, 128)
                        blue = (0, 100, 250)
                        count = 0
                        gameDisplay = pygame.display.set_mode((display_width, display_height))
                        pygame.display.set_caption("HelloKitty Garden")
                        fon = pygame.image.load('fon.png')
    window.fill(0)

    rect = gifFrameList[currentFrame].get_rect(center=(325, 250))
    window.blit(gifFrameList[currentFrame], rect)
    currentFrame = (currentFrame + 1) % len(gifFrameList)

    pygame.display.flip()