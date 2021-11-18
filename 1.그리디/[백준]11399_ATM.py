n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

cnt = 0
for time in time_list:
    cnt += n * time
    n -= 1
print(cnt)

# print(time_list)