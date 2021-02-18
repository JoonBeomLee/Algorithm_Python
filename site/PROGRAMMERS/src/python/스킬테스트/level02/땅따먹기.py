def solution(land):    
    
    for l_idx in range(0, len(land)-1):
        land[l_idx + 1][0] += max(land[l_idx][1], land[l_idx][2], land[l_idx][3])
        land[l_idx + 1][1] += max(land[l_idx][0], land[l_idx][2], land[l_idx][3])
        land[l_idx + 1][2] += max(land[l_idx][0], land[l_idx][1], land[l_idx][3])
        land[l_idx + 1][3] += max(land[l_idx][0], land[l_idx][1], land[l_idx][2])
        
    return max(land[len(land)-1])