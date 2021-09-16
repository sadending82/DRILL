from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')



isTimeToMoveCircle = False
RectMoveDirection = 0

PositionX = 400
PositionY = 90
CircleTime = 180

while True:

    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(PositionX, PositionY)
    
    if isTimeToMoveCircle == False:
        
        if RectMoveDirection == 0:
            PositionX += 2
            if PositionX >= 740:
                RectMoveDirection = 1
                
        elif RectMoveDirection == 1:
            PositionY += 2
            if PositionY >= 540:
                RectMoveDirection = 2
                
        elif RectMoveDirection == 2:
            PositionX -= 2
            if PositionX <= 60:
                RectMoveDirection = 3
                
        elif RectMoveDirection == 3:
            PositionY -= 2
            if PositionY <= 90:
                RectMoveDirection = 4
                
        elif RectMoveDirection == 4:
            PositionX += 2
            if PositionX >= 400:
                RectMoveDirection = 0
                isTimeToMoveCircle = True
    else:
        BaseX = 400
        BaseY = 300
        PositionX = BaseX - math.sin(CircleTime / 360 * 2 * math.pi) * 350 
        PositionY = BaseY - math.cos(CircleTime / 360 * 2 * math.pi) * 215 
        CircleTime += 1
        if(CircleTime >= 540):
            isTimeToMoveCircle = False
            CircleTime = 180
            PositionX = 400
            PositionY = 90

    delay(0.01)
                
            
            
