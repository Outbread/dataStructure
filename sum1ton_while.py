#1부터 n까지 정수의 합 구하기 (while)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요: '))

sum = 0

i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#1부터 n까지 정수의 합 구하기 (for)
#변수가 하나만 있을 때는 while보다 for문이 더 좋다.

print('sum from1 to n')
n = int(input('n값을 입력하세요:'))

sum = 0
i = 1
for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#값 정렬해서 정수 합 구하기
print('a~b 정수 합 구하기')
a = int(input('정수를 입력하세요: '))
b = int(input('정수를 입력하세요: '))

if a > b :
    a, b = b, a
    
sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지 합은 {sum}입니다.')