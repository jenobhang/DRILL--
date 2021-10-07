from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x=0
y=0

for i in range(100):
        angle = i*2*math.pi/100
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = 5*math.cos(angle/360 *2*math.pi)
        y = 5*math.sin(angle/360 *2*math.pi)
        delay(0.01)
        
    
       
        

    


    
        
    
