# # paper = list(map(int, input().split()))   # list() -> list 함수를 만들겠다.

# n, m, k = map(int, input().split())     # n : 배열의 크기, m : 숫자가 더해지는 횟수, k : 같은 수 더할 수 있는 횟수
# data = list(map(int, input().split()))


# data.sort()
# first_data = data[-1]
# second_data = data[-2]

# print(first_data)
# print(second_data)

# ans = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         ans += first_data
#         m -= 1
#     if m == 0:
#         break
#     ans += second_data
#     m -= 1

# print(ans)

n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
first_data = num_list[n - 1]
second_data = num_list[n - 2]

cnt = int(m / k + 1) * k
cnt += m % (k + 1)

result = 0
result += cnt * first_data
result += (m - cnt) * second_data
# print(m / (k + 1))
# print(m % (k + 1))
# print(m // (k + 1))
# print(int(m / (k + 1)))