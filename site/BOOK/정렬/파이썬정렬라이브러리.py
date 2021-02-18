array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted()
sorted_array = sorted(array)
print(sorted_array)

# sort()
array.sort()
print(array)

# 기준값으로 정렬
result = sorted(array, key=lambda x:x[0])