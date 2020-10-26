n = int(input())    # 입력된 금액
count = 0           # 거스름돈 동전 개수 count

coin_types = [500, 100, 50, 10]     # 가장 큰 단위의 화폐부터 차례대로 확인

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin           # 현재 동전으로 거스름돈을 제공한후 남은 돈

print(count)            # 카운트한 모든 동전의 개수