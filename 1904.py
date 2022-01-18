def solve():
    n = int(input())     # 입력값

    d = [0] * 1000001    # 배열 늘려주기 1 <= n <= 1000000

    d[1] = 1             # 초기값 설정
    d[2] = 2             # 초기값 설정

    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2] % 15746)
    print(d[n])

solve()

#d[n] = d[n-1] + d[n-2]