import math
import json

import p5

# Global varibles
t = 0   
path = []

# Initalizing data
result = open('/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/result.json', 'r')
x = json.load(result)
fourier = []

for i in x:
    freq = float(x[i]['freq'])
    amp = float(x[i]['amp'])
    phase = float(x[i]['phase'])
    
    temp = {}
    temp['freq'] = freq
    temp['amp'] = amp
    temp['phase'] = phase

    fourier.append(temp)


# p5 stuff
def setup():
    p5.size(1680, 1050)

def draw():
    global t
    global path
    global fourier_x
    global fourier_y

    p5.background(255)

    #Draw epicycles
    v = epicycle(750, 500, (math.pi / 2), fourier)
    path.insert(0, v)
    
    # Draw path
    p5.stroke(0)
    p5.begin_shape()
    p5.no_fill()
    for i in path:
        print(i[0], i[1])
        p5.vertex(i[0], i[1])
    p5.end_shape()
    
    # Time management
    dt = p5.TWO_PI / len(fourier)
    t += dt
    
    if t > 2 * math.pi:
        t = 0
        path = []
        p5.no_loop()
    
    p5.save_frame(f'/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/anh/.png')

def epicycle(x: int, y: int, offset: float, fourier: list) -> list:
    '''
    Draw a series of epicycles based on a list of dictionaries, which contain frequency, amplitude and phase of each cycle.
    
    Input:     
    - x, y: The original coornadinated.
    - offset: The first state of the first epicycle
    - fourier: The list, contained frequency, amplitude and phase of each cycle.
    
    Output: a list of the last x and y computed.
    '''
    for i in fourier:
        
        prevx = x
        prevy = y
        freq = i['freq']
        radius = i['amp']
        phase = i['phase']
        x += radius * math.cos(freq * t + phase + offset)
        y += radius * math.sin(freq * t + phase + offset)

        p5.stroke(0, 100)
        p5.no_fill()
        p5.circle((prevx, prevy), radius)

        
        p5.stroke(0, 50)
        p5.line(prevx,prevy,x,y)
    return [x , y]

if __name__ == '__main__':
    p5.run()
