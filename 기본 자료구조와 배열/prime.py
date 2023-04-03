#소수 찾기!!! 1000이하 소수 나열

cnt = 0     #곱셈과 나눗셈 합한 횟수
ptr = 0     #이미 찾은 소수의 개수
prime = [None] * 500

prime[ptr] = 2 #2는 소수
ptr += 1

prime[ptr] = 3 #3은 소수
ptr += 1

for n in range(5, 1001, 2):  #홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:
        cnt += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        cnt += 1
        
for i in range(ptr):
    print(prime[i])
