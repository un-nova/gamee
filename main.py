import pygame
import time
import cv2

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
pygame.init()

run = True
while run:
    clock.tick(7)
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
                    flower = pygame.image.load('flower.png')
                    flower.set_colorkey((255, 255, 255))
                    flower2 = pygame.image.load('flower.png')
                    flower2.set_colorkey((255, 255, 255))
                    window.blit(fon, (-300, -20))
                    window.blit(flower, (0, 250))
                    window.blit(flower2, (440, 250))


                    def autominer():
                        global coins
                        global autog
                        time.sleep(0.1)
                        coins = coins + autog


                    def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
                        font = pygame.font.Font('freesansbold.ttf', fsize)
                        text = font.render(text, True, Textcolor, Rectcolor)
                        textRect = text.get_rect()
                        textRect.center = (x, y)
                        window.blit(text, textRect)


                    kity = [pygame.image.load('kitty/pixil-frame-0.png'),
                            pygame.image.load('kitty/pixil-frame-1.png'),
                            pygame.image.load('kitty/pixil-frame-2.png'),
                            pygame.image.load('kitty/pixil-frame-3.png'),
                            pygame.image.load('kitty/pixil-frame-4.png'),
                            pygame.image.load('kitty/pixil-frame-5.png'),
                            pygame.image.load('kitty/pixil-frame-6.png'),
                            pygame.image.load('kitty/pixil-frame-7.png'),
                            pygame.image.load('kitty/pixil-frame-8.png'),
                            ]
                    window.blit(kity[0], (240, 260))

                    kur = [pygame.image.load('kuromi/pixil-frame-0.png'),
                              pygame.image.load('kuromi/pixil-frame-1.png'),
                              pygame.image.load('kuromi/pixil-frame-2.png'),
                              pygame.image.load('kuromi/pixil-frame-3.png'),
                              pygame.image.load('kuromi/pixil-frame-4.png'),
                              pygame.image.load('kuromi/pixil-frame-5.png'),
                              pygame.image.load('kuromi/pixil-frame-6.png'),
                              pygame.image.load('kuromi/pixil-frame-7.png'),
                              pygame.image.load('kuromi/pixil-frame-8.png'),
                              ]


                    def wind():
                        run = True
                        while run:
                            wind = pygame.image.load('window.png')
                            window.blit(wind, (100, 100))
                            if mopos >= (260, 0):
                                if mopos <= (400, 0):
                                    run = False
                        pygame.display.update()


                    def kuromi():
                        global count
                        run = True
                        while run:
                            window.blit(fon, (-300, -20))
                            window.blit(flower, (0, 250))
                            window.blit(flower2, (440, 250))
                            window.blit(kur[count], (240, 260))
                            DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150, 50,
                                     20)
                            DrawText("upgrade clicker ", black, light_blue, 530, 390, 20)
                            DrawText("buy auto miner ", black, light_blue, 120, 390, 20)
                            pygame.display.update()
                            if count == 8:
                                count = 0
                                run = False
                            else:
                                count += 1
                            pygame.display.update()
                            clock.tick(35)


                    def kitty():
                        global count
                        run = True
                        while run:
                            window.blit(fon, (-300, -20))
                            window.blit(flower, (0, 250))
                            window.blit(flower2, (440, 250))
                            window.blit(kity[count], (240, 260))
                            DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150, 50,
                                     20)
                            DrawText("upgrade clicker ", black, light_blue, 530, 390, 20)
                            DrawText("buy auto miner ", black, light_blue, 120, 390, 20)
                            pygame.display.update()
                            if count == 8:
                                count = 0
                                run = False
                            else:
                                count += 1
                            pygame.display.update()
                            clock.tick(35)


                    def main_loop():
                        global clock
                        global autog
                        global ver
                        global color1
                        global color2
                        global color3
                        mong = 1
                        cost = 50
                        cost2 = 50
                        num = 10
                        global coins
                        game_running = True
                        while game_running:
                            if game_running:
                                autominer()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    game_running = False

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mopos = pygame.mouse.get_pos()
                                    h = 30
                                    w = 30
                                    if mopos >= (260, 0):
                                        if mopos <= (400, 0):
                                            coins += mong
                                            if num == 10:
                                                kitty()
                                            if num == 100:
                                                kuromi()
                                    if mopos <= (600, 0):
                                        if mopos >= (500, 0):
                                            if coins >= cost:
                                                coins = coins - cost
                                                cost = cost * 1.5
                                                mong = mong * 1.1
                                                cost = round(cost, 0)

                                    if mopos >= (50, 0):
                                        if mopos <= (245, 0):
                                            if coins >= cost2:
                                                coins = coins - cost2
                                                cost2 = cost2 * 1.5
                                                autog = autog + 0.5
                                                cost2 = round(cost2, 0)
                                    if mopos >= (600, 0):
                                        if mopos <= (650, 30):
                                            wind()
                                    if coins == 2147483647:
                                        print("You Beat the game")
                                        game_running = False
                                    if coins != 5000:
                                        if coins > num:
                                            num = num * num
                            DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150, 50,
                                     20)
                            DrawText("upgrade clicker " + str(cost), black, light_blue, 530, 390, 20)
                            DrawText("Собери " + str(num) + " монет", black, light_blue, 530, 30, 20)
                            DrawText("buy auto miner " + str(cost2), black, light_blue, 120, 390, 20)
                            pygame.display.update()
                            clock.tick(20)


                    main_loop()
                    pygame.quit()
                    quit()
    window.fill(0)
    rect = gifFrameList[currentFrame].get_rect(center=(325, 250))
    window.blit(gifFrameList[currentFrame], rect)
    currentFrame = (currentFrame + 1) % len(gifFrameList)

    pygame.display.flip()
