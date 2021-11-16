import game_framework
from pico2d import *
import random

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
# 크기는 Boy에서 이미 지정해 주었기 때문에 모든 월드에서 똑같이 10 pixel 에 30cm 로 설정한다.

RUN_SPEED_KMPH = 60.0  # Km / Hour 60km/h의 속도로 설정한다.

RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5  # Action 한번 하는데 0.5초가 걸리도록 한다.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION  # 액션 한번 하는데 필요한 시간
FRAMES_PER_ACTION = 14  # 총 몇 프레임 인가?


#  FRAMES_PER_ACTION * ACTION_PER_TIME 이 날개짓 속도이다.


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(300, 500)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = random.randint(1, 12)
        self.event_que = []

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        #  FRAMES_PER_ACTION * ACTION_PER_TIME = 날개짓 속도이다.
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.x > 1550:
            self.dir *= -1
        elif self.x < 50:
            self.dir *= -1

        self.x = clamp(50, self.x, 1550)

        self.velocity = RUN_SPEED_PPS * self.dir
        self.x += self.velocity * game_framework.frame_time
        print('x=', self.x, 'y=', self.y)

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, '', self.x, self.y, 100,
                                           100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100,
                                           100)
