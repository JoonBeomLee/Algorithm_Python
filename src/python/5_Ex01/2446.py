star_cnt = int(input())

for i in range(star_cnt*2):
    # reverse tri
    if i <= star_cnt-1:
        for left_blank in range(i):
            print(' ', end='')

        for star in range(star_cnt*2-1-i*2):
            print('*', end='')
        """
        for right_blank in range(i):
            print(' ', end='')
        """    
        print()

    #center
    elif(i == star_cnt):
        continue
        
    # tri
    else:
        for left_blank in range(star_cnt*2-i-1):
            print(' ', end='')
            
        for star in range(i-(star_cnt*2-i-1)):
            print('*', end='')
        """    
        for right_blank in range(star_cnt*2-i-1):
            print(' ', end='')
        """    
        print()