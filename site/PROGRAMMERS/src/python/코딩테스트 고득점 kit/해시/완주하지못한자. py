def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            answer = participant[idx]
            return answer
                    
    return participant[-1]