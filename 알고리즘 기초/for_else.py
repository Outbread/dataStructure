# 10~99사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('프로그램을 중단합니다.')
        break
else:
    print('\n난수생성을 종료합니다.')
    
# 1~12까지 8을 건너뛰고 출력하기

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
    
print()

##이런 식의 작성은 수가 커지면 비효율적입니다. 숫자를 하나 건너뛰게 하려고 큰 수 모두 판단해야하기 때문입니다.
##그냥 리스트를 사용해서 8을 건너뜁시다.

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()