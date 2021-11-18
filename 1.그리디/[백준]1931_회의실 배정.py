n = int(input())    # n : 회의의 수
room = []

for _ in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

######### array.sort(key = lambda x:x[0]) #########


room.sort(key = lambda x:x[0])
room.sort(key = lambda x:x[1])
# print("종료시간 기준 정렬")
# print(room)

cnt = 1
end_point = room[0][1]
for i in range(1, n):
    if room[i][0] >= end_point:
        cnt += 1
        end_point = room[i][1]
print(cnt)