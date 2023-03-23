#양수만 입력받아 1부터 입력받은 값 까지 정수의 합 구하기
print('1부터 n까지 정수의 합 구하기')

while True:
    n = int(input('n값을 입력하세요 : '))
    if n > 0:
        break
    
sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1
    
print(f'1부터 {n}까지 정수의 합은{sum}입니다.')

#가로세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형 넒이를 입력하세요 : '))

for i in range(1, area + 1):
    if i * i > area: break
    if area % i: continue
    print(f'{i} * {area // i}')