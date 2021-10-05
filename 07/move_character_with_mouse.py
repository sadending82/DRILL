from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def SetHandPos():
    global handX, handY

    handX, handY = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)


def SetCharPos():
    global x, y
    global moveX, moveY
    global direction

    if x == handX and y == handY:
        SetHandPos()

    if handX - x > 0:
        direction = 1
    else:
        direction = -1

    moveX = (handX - x) // 30
    moveY = (handY - y) // 30


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:  # x, y = event.x, KPU_HEIGHT - 1 - event.y
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

handX, handY = x, y

moveX, moveY = 0, 0

direction = 0

frame = 0

# hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if abs(handX-x) < 30 and abs(handY-y) < 30:
        x, y = handX, handY
        SetCharPos()

    x += moveX
    y += moveY

    hand_arrow.draw(handX, handY)

    if direction == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    update_canvas()

    frame = (frame + 1) % 8

    delay(1 / 60)
    handle_events()

close_canvas()
