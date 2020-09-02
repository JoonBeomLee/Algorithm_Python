def calc_step(num):
    limit = 1
    up = 1; down = 1; step = 1; direction = "down"
    result = str(up) + "/" + str(down)
    
    while True:
        if(limit == num): return result
        step += 1
        
        if(direction == "down"):
            up = 1; down = step
            for i in range(1, step + 1):
                limit += 1
                #print("down" + str(up) + "/" + str(down))
                if(limit == num): result = str(up) + "/" + str(down); break
                up += 1; down -= 1; 

            direction = "up"
            
        elif(direction == "up"):
            up = step; down = 1
            for i in range(1, step + 1):
                limit += 1
                #print("up" + str(up) + "/" + str(down), i, step)
                if(limit == num): result = str(up) + "/" + str(down); break
                up -= 1; down += 1;

            direction = "down"