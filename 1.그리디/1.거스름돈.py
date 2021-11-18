# coin_list = (500, 100, 50, 10)

# n = int(input())
# cnt = 0

# for coin in coin_list:
#     cnt += n // coin
#     n %= coin
#     print("coin")
#     print(coin)
#     print("n")
#     print(n)
#     print("cnt")
#     print(cnt)

# print(cnt)

coin_list = (500, 100, 50, 10)
n = int(input())
cnt = 0
print(type(coin_list))
for coin in coin_list:
    cnt += n // coin
    n %= coin

print(cnt)