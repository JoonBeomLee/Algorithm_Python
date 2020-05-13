def init_map():
    count = 1
    new_map = list()
    i = 1
    
    while(count <= 2000000000):
        new_map.append(count)
        count = count + (i * 6)
        i += 1
        
    return new_map

def found_dist(dist, number):
    count = 1
    
    if(number == 1): return count
    
    for i in range(len(dist) - 1):
        count = count + 1
        if(dist[i] <= number and number <= dist[i+1]):
            break;
            
    return count
    
dist_map = init_map()
print(found_dist(dist_map, int(input())))