from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle() :
    print('CIRCLE')
    
    cx = 800 / 2
    cy = 600 / 2
    r = 200
    for deg in range(0, 360, 5) :
        x = cx + r * math.cos(deg * 2 * math.pi / 360)
        y = cy + r * math.sin(deg * 2 * math.pi / 360)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

def run_rectangle() :
    print('RENTANGLE')
    pass

while (True) :
    run_circle()
    run_rectangle()
    break

close_canvas()
