import collections

def solution(clothes):
    answer = 1
    closet_arr = {}
    for i in clothes:
        if i[1] in closet_arr: closet_arr[i[1]] += 1
        else: closet_arr[i[1]] = 1
        
    print(closet_arr)
        
    for clothes_count in closet_arr.values():
        answer *= (clothes_count+1)
        
    return answer - 1