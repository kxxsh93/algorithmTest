n, k = map(int, input().split())
list = []
cnt = 0
for coin in range(n):
    coin = int(input())
    list.append(coin)

list.sort(reverse=True)
while k != 0:
    for coin in list:
        cnt += k // coin
        k %= coin


print(cnt)
# print(lllist)
