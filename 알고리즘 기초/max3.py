# 세 정수 입력받아 최댓값구하기

print('세 정수 최댓값 구하기')
a = int(input('정수 a값을 입력하세요 : '))
b = int(input('정수 b값을 입력하세요 : '))
c = int(input('정수 c값을 입력하세요 : '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최대값은 {maximum}입니다.')

#문자열과 숫자 입력받기
print('이름을 입력하세요: ', end='')
name = input()
print(f'hi, {name}')

