import pygame
import cv2
from random import randint
from typing import Tuple

pygame.init()

pygame.mixer.music.load('sounds/start.mp3')
pygame.mixer.music.play(-1)

pygame.display.set_caption('HelloKitty Garden')

mouse_counter = 0
need_drow_click = False
mouse_size = int(87)

chor_ef = [pygame.image.load('chors_ef/pixil-frame-0.png'),
           pygame.image.load('chors_ef/pixil-frame-1.png'),
           pygame.image.load('chors_ef/pixil-frame-2.png'),
           pygame.image.load('chors_ef/pixil-frame-3.png'),
           pygame.image.load('chors_ef/pixil-frame-4.png'),
           ]


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


window = pygame.display.set_mode((650, 500))
clock = pygame.time.Clock()


def draw_mouse():
    global mouse_counter, need_drow_click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[0] or click[1]:
        need_drow_click = True

    if mouse_counter == 5:
        mouse_counter = 0
        need_drow_click = False

    if need_drow_click:
        drow_x = mouse[0] - 87 // 2
        drow_y = mouse[1] - 87 // 2

        window.blit(chor_ef[mouse_counter], (drow_x, drow_y))
        mouse_counter += 1
        pygame.display.update()
        clock.tick(35)


gifFrameList = loadGIF(r"pix.gif")
currentFrame = 0


def rul():
    rules = pygame.image.load('rules.png')
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            elif e.type == pygame.KEYDOWN and e.key == pygame.K_q:
                running = False

        window.blit(rules, (0, 0))
        pygame.display.flip()


run = True
while run:
    draw_mouse()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            rul()
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
                    blue = (0, 100, 250)
                    count = 0
                    t = 2
                    gameDisplay = pygame.display.set_mode((display_width, display_height))
                    pygame.display.set_caption("HelloKitty Garden")
                    fon = pygame.image.load('fon.png')
                    flower = pygame.image.load('flower.png')
                    flower.set_colorkey((255, 255, 255))
                    flower2 = pygame.image.load('flower.png')
                    flower2.set_colorkey((255, 255, 255))
                    window.blit(fon, (-300, -20))
                    window.blit(flower, (40, 250))
                    window.blit(flower2, (440, 250))
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sounds/base game.mp3')
                    pygame.mixer.music.play(-1)


                    def autominer():
                        global coins
                        global autog
                        global t
                        if t % 2 == 0:
                            coins = coins + autog
                            t += 0.5
                        else:
                            t += 0.5


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

                    melody = [pygame.image.load('my_melody/pixil-frame-0.png'),
                              pygame.image.load('my_melody/pixil-frame-1.png'),
                              pygame.image.load('my_melody/pixil-frame-2.png'),
                              pygame.image.load('my_melody/pixil-frame-3.png'),
                              pygame.image.load('my_melody/pixil-frame-4.png'),
                              pygame.image.load('my_melody/pixil-frame-5.png'),
                              pygame.image.load('my_melody/pixil-frame-6.png'),
                              pygame.image.load('my_melody/pixil-frame-7.png'),
                              pygame.image.load('my_melody/pixil-frame-8.png'),
                              ]

                    kero = [pygame.image.load('keroppi/pixil-frame-0.png'),
                            pygame.image.load('keroppi/pixil-frame-1.png'),
                            pygame.image.load('keroppi/pixil-frame-2.png'),
                            pygame.image.load('keroppi/pixil-frame-3.png'),
                            pygame.image.load('keroppi/pixil-frame-4.png'),
                            pygame.image.load('keroppi/pixil-frame-5.png'),
                            pygame.image.load('keroppi/pixil-frame-6.png'),
                            pygame.image.load('keroppi/pixil-frame-7.png'),
                            pygame.image.load('keroppi/pixil-frame-8.png'),
                            ]

                    cinnam = [pygame.image.load('cinnamoroll/pixil-frame-0.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-1.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-2.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-3.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-4.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-5.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-6.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-7.png'),
                              pygame.image.load('cinnamoroll/pixil-frame-8.png'),
                              ]


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
                        lvl = 1

                        class Player(pygame.sprite.Sprite):
                            def __init__(self):
                                super(Player, self).__init__()
                                self.surf = pygame.image.load('heart.png').convert_alpha()
                                self.rect = self.surf.get_rect()

                            def update(self, pos: Tuple):
                                self.rect.center = pos

                        class Coin(pygame.sprite.Sprite):
                            def __init__(self):
                                super(Coin, self).__init__()
                                self.surf = coin_image = pygame.image.load('flover.png').convert_alpha()
                                self.rect = self.surf.get_rect(
                                    center=(
                                        randint(10, WIDTH - 10),
                                        randint(10, HEIGHT - 10),
                                    )
                                )

                        def kuromi():
                            global count
                            run = True
                            while run:
                                window.blit(fon, (-300, -20))
                                window.blit(flower, (40, 230))
                                window.blit(flower2, (450, 230))
                                window.blit(kur[count], (240, 260))
                                DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150,
                                         50,
                                         20)
                                DrawText("upgrade clicker " + str(cost), black, light_blue, 530, 390, 20)
                                DrawText("lvl " + str(lvl) + " собери " + str(num) + " монет", black, light_blue,
                                         530,
                                         50,
                                         20)
                                DrawText("buy auto miner " + str(cost2), black, light_blue, 120, 390, 20)
                                for coin in coin_list:
                                    window.blit(coin.surf, coin.rect)
                                window.blit(player.surf, player.rect)
                                pygame.display.update()
                                if count == 8:
                                    count = 0
                                    run = False
                                else:
                                    count += 1
                                autominer()
                                pygame.display.update()
                                clock.tick(35)

                        def kitty():
                            global count
                            run = True
                            while run:
                                window.blit(fon, (-300, -20))
                                window.blit(flower, (40, 230))
                                window.blit(flower2, (450, 230))
                                window.blit(kity[count], (240, 260))
                                DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150,
                                         50,
                                         20)
                                DrawText("upgrade clicker " + str(cost), black, light_blue, 530, 390, 20)
                                DrawText("lvl " + str(lvl) + " собери " + str(num) + " монет", black, light_blue,
                                         530,
                                         50,
                                         20)
                                DrawText("buy auto miner " + str(cost2), black, light_blue, 120, 390, 20)
                                for coin in coin_list:
                                    window.blit(coin.surf, coin.rect)
                                window.blit(player.surf, player.rect)
                                pygame.display.update()
                                if count == 8:
                                    count = 0
                                    run = False
                                else:
                                    count += 1
                                autominer()
                                pygame.display.update()
                                clock.tick(35)

                        def my_melody():
                            global count
                            run = True
                            while run:
                                window.blit(fon, (-300, -20))
                                window.blit(flower, (40, 230))
                                window.blit(flower2, (450, 230))
                                window.blit(melody[count], (240, 260))
                                DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150,
                                         50,
                                         20)
                                DrawText("upgrade clicker " + str(cost), black, light_blue, 530, 390, 20)
                                DrawText("lvl " + str(lvl) + " собери " + str(num) + " монет", black, light_blue,
                                         530,
                                         50,
                                         20)
                                DrawText("buy auto miner " + str(cost2), black, light_blue, 120, 390, 20)
                                for coin in coin_list:
                                    window.blit(coin.surf, coin.rect)
                                window.blit(player.surf, player.rect)
                                pygame.display.update()
                                if count == 8:
                                    count = 0
                                    run = False
                                else:
                                    count += 1
                                autominer()
                                pygame.display.update()
                                clock.tick(35)

                        def keroppi():
                            global count
                            run = True
                            while run:
                                window.blit(fon, (-300, -20))
                                window.blit(flower, (40, 230))
                                window.blit(flower2, (450, 230))
                                window.blit(kero[count], (240, 260))
                                DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150,
                                         50,
                                         20)
                                DrawText("upgrade clicker " + str(cost), black, light_blue, 530, 390, 20)
                                DrawText("lvl " + str(lvl) + " собери " + str(num) + " монет", black, light_blue,
                                         530,
                                         50,
                                         20)
                                DrawText("buy auto miner " + str(cost2), black, light_blue, 120, 390, 20)
                                for coin in coin_list:
                                    window.blit(coin.surf, coin.rect)
                                window.blit(player.surf, player.rect)
                                pygame.display.update()
                                if count == 8:
                                    count = 0
                                    run = False
                                else:
                                    count += 1
                                autominer()
                                pygame.display.update()
                                clock.tick(35)

                        def cinnamoroll():
                            global count
                            run = True
                            while run:
                                window.blit(fon, (-300, -20))
                                window.blit(flower, (40, 230))
                                window.blit(flower2, (450, 230))
                                window.blit(cinnam[count], (240, 260))
                                DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black, light_blue, 150,
                                         50,
                                         20)
                                DrawText("upgrade clicker " + str(cost), black, light_blue, 530, 390, 20)
                                DrawText("lvl " + str(lvl) + " собери " + str(num) + " монет", black, light_blue,
                                         530,
                                         50,
                                         20)
                                DrawText("buy auto miner " + str(cost2), black, light_blue, 120, 390, 20)
                                for coin in coin_list:
                                    window.blit(coin.surf, coin.rect)
                                window.blit(player.surf, player.rect)
                                pygame.display.update()
                                if count == 8:
                                    count = 0
                                    run = False
                                else:
                                    count += 1
                                autominer()
                                pygame.display.update()
                                clock.tick(35)

                        def ending():
                            global autog
                            global coins
                            global lvl
                            run = True
                            while run:
                                for e in pygame.event.get():
                                    if e.type == pygame.QUIT:
                                        run = False

                                    elif e.type == pygame.KEYDOWN and e.key == pygame.K_q:
                                        run = False
                                        autog = 0
                                        coins = 0
                                        lvl = 1
                                        main_loop()

                                en = pygame.image.load('game over.png')
                                window.blit(en, (0, 0))
                                pygame.display.flip()

                        coin_countdown = 2500
                        coin_interval = 100
                        WIDTH = 650
                        HEIGHT = 500
                        COIN_COUNT = 10
                        pers = kity
                        global coins
                        game_running = True
                        while game_running:
                            if game_running:
                                pygame.mouse.set_visible(False)
                                clock = pygame.time.Clock()
                                ADDCOIN = pygame.USEREVENT + 1
                                pygame.time.set_timer(ADDCOIN, coin_countdown)

                                coin_list = pygame.sprite.Group()
                                player = Player()
                                player.update(pygame.mouse.get_pos())

                                running = True
                                while running:
                                    autominer()
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            running = False

                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mopos = pygame.mouse.get_pos()
                                            if mopos >= (260, 0):
                                                if mopos <= (400, 0):
                                                    coins += mong
                                                    if lvl == 1:
                                                        kitty()
                                                    if lvl == 2:
                                                        pers = kur
                                                        kuromi()
                                                    if lvl == 3:
                                                        pers = cinnam
                                                        cinnamoroll()
                                                    if lvl == 4:
                                                        pers = melody
                                                        my_melody()
                                                    if lvl == 5:
                                                        pers = kero
                                                        keroppi()
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
                                                        autog = autog + 0.2
                                                        cost2 = round(cost2, 0)

                                            if coins < 160:
                                                if coins > num - 1:
                                                    lvl += 1
                                                    num = num * 2
                                            else:
                                                DrawText("YOU WIN ", black, light_blue, 320, 250, 90)
                                                game_running = False
                                        elif event.type == ADDCOIN:
                                            new_coin = Coin()
                                            coin_list.add(new_coin)

                                            if len(coin_list) < 3:
                                                coin_countdown -= coin_interval
                                            if coin_countdown < 100:
                                                coin_countdown = 100
                                            pygame.time.set_timer(ADDCOIN, 0)

                                            pygame.time.set_timer(ADDCOIN, coin_countdown)

                                    player.update(pygame.mouse.get_pos())

                                    coins_collected = pygame.sprite.spritecollide(
                                        sprite=player, group=coin_list, dokill=True
                                    )
                                    for coin in coins_collected:
                                        coins += 10

                                    if len(coin_list) >= COIN_COUNT:
                                        ending()
                                        running = False
                                    window.blit(fon, (-300, -20))
                                    window.blit(flower, (40, 230))
                                    window.blit(flower2, (450, 230))
                                    window.blit(pers[count], (240, 260))
                                    DrawText("you have " + str(f'{coins:.2f}') + " flower coins", black,light_blue,
                                             150,
                                             50,
                                             20)
                                    DrawText("upgrade clicker " + str(cost), black,light_blue,  530, 390, 20)
                                    DrawText("lvl " + str(lvl) + " собери " + str(num) + " монет", black,light_blue,
                                             530,
                                             50,
                                             20)
                                    DrawText("buy auto miner " + str(cost2), black,light_blue,  120, 390, 20)
                                    for coin in coin_list:
                                        window.blit(coin.surf, coin.rect)
                                    window.blit(player.surf, player.rect)
                                    pygame.display.flip()

                                    clock.tick(30)

                                print(f"Game over! Final score: {coins}")

                                pygame.mouse.set_visible(True)
                                pygame.quit()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    game_running = False
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
