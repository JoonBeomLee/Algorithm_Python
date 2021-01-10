# H 입력
H = int(input())

# 결과값 count
count = 0

# 0시 0분 0초 ~ H시 59분 59초
# 시 0 ~ H
for i in range(H + 1):
    # 분 0 ~ 59
    for j in range(60):
        # 초 0 ~ 59
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

# 결과 출력
print(count)