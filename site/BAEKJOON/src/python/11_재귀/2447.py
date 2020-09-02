import sys
design = int(input())

def draw(design):
    for i in range(design):
        for j in range(design):
            draw_in(i, j)
        print()
        
def draw_in(i, j):
    while(i != 0):
        if(i % 3 == 1 and j % 3 == 1):  
            print(" ", end="")
            return
        
        i = i // 3
        j = j // 3
    print("*", end="")
        
draw(design)