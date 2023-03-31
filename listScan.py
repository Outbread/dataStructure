# 리스트 원소 스캔!

#1
x = ['a', 'b', 'c', 'd']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
#2

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
    
#3

for i, name in enumerate(x,1):
    print(f'{i}번째 = {name}')

#4

for i in x:
    print(i)