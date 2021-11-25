import json

data = open('/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/result.txt', 'r')
result = open('/home/supperman/Documents/linhtinh/(Python) Fourier Transform and Epicycle/result.json', 'a')

result.truncate(0)

x_data = data.read().split('\n')

result_dict_x = {}

for i in range(len(x_data)-1):
    temp = x_data[i].split()
    result_dict_x[i] = {'freq': temp[0], 'amp': temp[1], 'phase': temp[2]}


json.dump(result_dict_x, result, indent = 4)

data.close()
result.close()

print('Done!')
