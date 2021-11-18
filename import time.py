# import time
# start_time = time.time()

# for i in range(10):
#     for j in range(100):
#         m = i + j
#         print(m)



# end_time = time.time()
# print (end_time - start_time)

# from random import randint
# import time

# array = []
# for _ in range(10000):
#     array.append(randint(1, 100))
# print(array)
# start_time = time.time()


# for i in range(len(array)):
#     min_idx = i
#     for j in range(i + 1, len(array)):
#         if array[min_idx] > array[j]:
#             min_idx = j
#     array[i], array[min_idx] = array[min_idx], array[i]

# end_time = time.time()            
# print("선택 정렬 성능 시간 측정 : ", end_time - start_time)

# start_time = time.time()
# array.sort()

# end_time = time.time()

# print("기본 정렬 성능 시간 측정 :", end_time - start_time)

from random import randint
import copy
import time

array = []
for _ in range(10000):
    array.append(randint(1,100))

array1 = copy.deepcopy(array)
start_time = time.time()
print(start_time)

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

end_time = time.time()

print("선택 정렬 기능 시간 측정 :", end_time - start_time)
print(end_time)


start_time = time.time()
print(start_time)
array1.sort()
end_time = time.time()
print(end_time)

print("기존 정렬 기능 시간 측정 :", end_time - start_time)