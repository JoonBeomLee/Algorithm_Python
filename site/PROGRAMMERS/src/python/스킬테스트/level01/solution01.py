def solution(arr):
    answer = []

    for idx in range(len(arr)):
        if idx + 1 >= len(arr): 
            answer.append(arr[idx])
            continue

        elif arr[idx] != arr[idx+1]:
            answer.append(arr[idx])


    return answer