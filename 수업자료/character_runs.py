from pico2d import *
import random

class BigBall:
    def __init__(self):
        self.x = random.randint(21, 780)
        self.y = 599
        self.speed = random.randint(1, 4)
        self.stopy = 71
        self.image = load_image('ball41x41.png')

    def loop(self):
        self.image.draw(self.x, self.y)
        if self.y <= 71:
            speed = 0
            self.y = self.stopy

        self.y -= self.speed

class SmallBall:
    def __init__(self):
        self.x = random.randint(21, 780)
        self.y = 599
        self.speed = random.randint(1, 4)
        self.stopy = 51
        self.image = load_image('ball21x21.png')

    def loop(self):
        self.image.draw(self.x, self.y)
        if self.y <= 51:
            speed = 0
            self.y = self.stopy

        self.y -= self.speed


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

BigballCount = random.randint(3, 12)

Bballs = [ BigBall() for n in range(BigballCount)]
Sballs = [ SmallBall() for n in range(20-BigballCount)]

x = 0
frame = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    for i in Bballs:
        i.loop()
    for i in Sballs:
        i.loop()
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()


close_canvas()

