import json

train = open('/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/test.json', 'r')
x = open('/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/x.txt', 'a')
y = open('/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/y.txt', 'a')

x.truncate(0)
y.truncate(0)

data = json.load(train)
short = data['drawing']

skip = int(input())

for i in range(0, len(short), skip):
    print(short[i])
    x.write(f'{short[i]["x"]}\n')
    y.write(f'{short[i]["y"]}\n')

train.close()
x.close()
y.close()

print(f'These file contains {i/skip} numbers!')
print('Done!')
