import math

x = []
y = []

def dft(re_list: list, im_list: list) -> list:
    '''
    Input: Two lists, which contains real and imagine component (both as float) of inputs.
    Output: A list of lists, which contains three elements: frequency, amplitude and phase of each epicycle.
    '''
    X = []
    N = len(x)
    k = 0
    n = 0
    
    for k in range(N):
        re = 0
        im = 0
        
        for n in range(N):
            phi = ((2 * math.pi) / N) * k * n
            re += re_list[n] * math.cos(phi) + im_list[n] * math.sin(phi)
            im -= re_list[n] * math.sin(phi) - im_list[n] * math.cos(phi)
        re = re / N
        im = im / N
        freq = k
        amp = math.sqrt(re * re + im * im)
        phase = math.atan2(im, re)
        result = [freq, amp, phase]
        X.append(result)
    return X

with open('./x.txt', 'r') as x_data:
    x = x_data.read().split('\n')
    temp = [float(i) for i in x if i != '']
    x = temp
    

with open('./y.txt', 'r') as y_data:
    y = y_data.read().split('\n')
    temp = [float(i) for i in y if i != '']
    y = temp

result = dft(x, y)

with open('./result.txt', 'a') as result_file:
    result_file.truncate(0)
    for i in result:
        result_file.write(f'{i[0]} {i[1]} {i[2]} \n')

print('Done!')
