from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x, y) :
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01) 

def run_circle() :
    print('CIRCLE')
    
    cx = 800 / 2
    cy = 600 / 2
    r = 200
    for deg in range(0, 360, 5) :
        x = cx + r * math.cos(deg * 2 * math.pi / 360)
        y = cy + r * math.sin(deg * 2 * math.pi / 360)
        render_all(x, y)

def run_rectangle() :
    print('RENTANGLE')

    # bottom line 
    for x in range(50, 750 + 1, 10) :
        render_all(x, 90)

    # right line
    for y in range(90, 540 + 1, 10) :
        render_all(x, y)

    # top line    
    for x in range(750, 50 - 1, -10) :
        render_all(x, y)

    # left line
    for y in range(540, 90 - 1, -10) :
        render_all(x, y)

while (True) :
    run_circle()
    run_rectangle()
    break

close_canvas()
