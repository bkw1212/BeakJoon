def solve():
    t = int(input())  # 테스트 케이스 입력 받기
    value = 0         # 최대값만 필요하니 최소값 저장(초기값)
    arr = []          # 입력값 저장할 배열 공간
    for _ in range(t):
        a = int(input())
        arr.append(a)           # 입력값 저장
        value = max(value, a)   # 입력받은 값중 최대값을 value에 저장

    rst = [1, 1, 1, 2, 2]       # Sn-5

    for i in range(5, value):      # 5번 부터 value까지
        tmp = rst[i-1] + rst[i-5]
        rst.append(tmp)

    for i in range(t):
        print(rst[arr[i]-1])       # rst의 index에 맞게 자리값 맞춰 출력

solve()

# Sn = Sn-1 + Sn-5
# Sn = Sn-2 + Sn-3