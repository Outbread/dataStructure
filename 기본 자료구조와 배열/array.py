# 시퀀스 원소의 최댓값 출력
## max_of()를 사용했다.

from typing import Any, Sequence ##any는 제약이 없는 임의의 자료형, Sequence는 list, tuple, bytearry, str type이 있다.

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 요소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__': ##다른 곳에서 import해도 이것이 실행되지 않게 했다. 
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num    # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')
