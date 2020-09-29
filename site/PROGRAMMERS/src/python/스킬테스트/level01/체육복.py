def solution(n, lost, reserve):
    answer = 0
    mult_std = []
    solve_count = 0
    
    reserve.sort()
    lost.sort()
    
    for lst_std in lost:
        if lst_std in reserve: mult_std.append(lst_std)
            
    for mult in mult_std:
        lost.remove(mult)
        reserve.remove(mult)
    
    for lst_std in lost:
        if lst_std - 1 in reserve:  solve_count += 1; reserve.remove(lst_std - 1); continue 
        if lst_std in reserve:  solve_count += 1; reserve.remove(lst_std); continue
        if lst_std + 1 in reserve:  solve_count += 1; reserve.remove(lst_std + 1); continue
            
    answer = n - len(lost) + solve_count
    return answer