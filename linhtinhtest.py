import math
import random
import p5

# Global varibles
t = 0   
path = []

# Discrete Fourier Transform.
def dft(x: list) -> list : 
    t = []
    N = len(x)
    for k in range(N):
        re = 0
        im = 0
        a = 0
        for n in range(N):
            phi = (2* math.pi * k * n) / N
            re += x[n] * math.cos(phi)
            im -= x[n] * math.sin(phi)
        re = re / N
        im = im / N
        freq = k
        amp = math.sqrt(re*re+im*im)
        phase = math.atan2(im, re)
        t.append(
            {
            'freq': freq,
            'amp': amp,
            'phase': phase
            }
        )
    return t

print('Calculate data...')
#x_data = open('x.txt', 'r')
#y_data = open('x.txt', 'r')
#x_raw = x_data.read().split()
#y_raw = y_data.read().split()
#x = [float(i) for i in x_raw if i]
#y = [float(i) for i in y_raw if i]


fourier_x = dft(x)
fourier_y = dft(y)
print(fourier_x)
print(fourier_y)
print('Done!')

# p5 stuff
def setup():
    p5.size(800, 600)



def draw():
    global t
    global path
    global fourier_x
    global fourier_y

    p5.background(0)

    #Draw epicycles
    vx = epicycle(500, 100, 0, fourier_x)
    vy = epicycle(100, 300, (math.pi / 2), fourier_y)
    v = [vx[0], vy[1]] 
    path.insert(0, v)
    
    # Draw lines
    p5.line(vx[0], vx[1], v[0], v[1])
    p5.line(vy[0], vy[1], v[0], v[1])
    p5.begin_shape()
    p5.no_fill()
    for i in path:
        print(i)
        p5.vertex(i[0], i[1])
    p5.end_shape()
    
    # Time management
    dt = p5.TWO_PI / len(fourier_y)
    t += dt

    if t > 2 * math.pi:
        t = 0
        path = []

def epicycle(x: int, y: int, offset: float, fourier: list) -> list:
    for i in fourier:
        prevx = x
        prevy = y
        freq = i['freq']
        radius = i['amp']
        phase = i['phase']
        x += radius * math.cos(freq * t + phase + offset)
        y += radius * math.sin(freq * t + phase + offset)

        p5.stroke(255, 100)
        p5.no_fill()
        p5.circle((prevx, prevy), radius)

        
        p5.stroke(255)
        p5.line(prevx,prevy,x,y)
    return [x , y]

if __name__ == '__main__':
    p5.run()
