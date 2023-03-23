# #반복 과정에서 조건 판단하기
# ## + 와 - 를 번갈아 출력해보자

# print('+ 와 - 를 번갈아 출력해보자')
# n = int(input('how many do I return?'))

# for i in range(n):
#     if i % 2:
#         print('-', end='')
#     else:
#         print('+', end='')
# print()

# ### for문이 반복될 때 마다 if문을 수행하기 때문에 수가 커지면 if문 수행도 많아진다. 그렇다면 아래처럼 해보자.

# n = int(input('how many do I return?'))

# for _ in range(n // 2):
#     print('+-', end='')

# if n % 2:
#     print('+', end='')

# print()

### 이렇게 변경하면 반복문에서 조건문을 수행하지 않아 효율적이고, 카운터용 변수를 0에서 1로 변경해도 유연하게 대응할 수 있다.
### range()함수의 인수만 수정하면 되기 때문이다.

#*를 n개 출력하되 w개마다 줄바꿈하기
print('*를 출력합니다.')
n = int(input('how many do I return?: '))
w = int(input('when do I operate enter?: '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()

## 이것 또한 반복문에서 조건문을 계속 실행하게 되므로 효율적이지 않아 아래와 같이 쓰면 더 좋다

print('*를 출력합니다.')
n = int(input('how many do I return?: '))
w = int(input('when do I operate enter?: '))

for _ in range( n // w):
    print('*' * w)
    
rest = n % w
if rest:
    print('*' * rest)

