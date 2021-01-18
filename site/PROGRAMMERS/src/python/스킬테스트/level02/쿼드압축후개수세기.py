check_map = list()

def zip_check(_map, h, w, size):
    global check_map
    
    tmp = _map[h][w]
    
    if(size == 1):
        check_map[tmp] += 1
        return
    
    mergable = True
    
    for i in range(h, h + size):
        for j in range(w, w + size):
            
            if _map[h][w] != size: mergable = False

    if mergable:
        check_map[tmp] += 1
    else:
        size = int(size / 2)
        zip_check(_map, h, w, size)
        zip_check(_map, h, w + size, size)
        zip_check(_map, h + size, w, size)
        zip_check(_map, h + size, w + size, size)
        
                
def solution(arr):
    answer = []
    
    h = len(arr)
    w = len(arr[0])
    print(h, w)
    
    zip_check(arr, 0, 0, h * w)
    
    print(check_map)
    
    return answer