from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
        
# 원소의 순서를 바꾸기 위해서는 범위를 나누기 2 해준다. 그리고 맨 끝 원소는 [전체길이 -  인덱스순서 - 1] 이다. 
# 총길이가 7일경우, 0,1,2,3,4,5,6 이므로 뒤에서 두번째의 인덱스는 7 - 1 - 1 = 5 이다.
    