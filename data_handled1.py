import json

train = open('../test.json', 'r')
x = open('../x.txt', 'a')
y = open('../y.txt', 'a')

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
