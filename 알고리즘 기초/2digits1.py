#2자리 양수 입력받기

print('2자리 양수 입력받기')

while True:
    no = int(input('값을 입력하세요: '))
    if no >= 10 and no <= 99:
        break
print(f'입력받은 양수는 {no}')

#구구단 출력하기

print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end=' ')
    print()
    
print('-' * 27)

# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('왼쪽 아래가 직각인 이등변 삼각형으로 출력')
n = int(input('짧은 변의 길이를 입력하세요: '))

for i in range(n):
    for _ in range(i + 1):
        print('*', end='')
    print()
    
# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('-' * 28)

n = int(input('짧은 변의 길이를 입력하세여: '))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()
        