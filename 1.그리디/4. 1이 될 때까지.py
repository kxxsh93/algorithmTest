# # 내 풀이 1.
# n, k = map(int, input().split())
# cnt = 0

# while True:
#     if n % k == 0:
#         n //= k
#         cnt += 1
#         print(n)
#     elif n == 1:
#         break
#     else:
#         n -= 1
#         cnt += 1
#         print(n)

# print(cnt)

# # Example
# print(19 // 5)
# print(19 / 5)
# print(19 % 5)

# # 이해하고 다시 보기 p88
# n, k = map(int, input().split())
# result = 0

# while True:
