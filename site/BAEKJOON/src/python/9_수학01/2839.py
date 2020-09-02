sugar = int(input())

def count_sugar_box(sugar):
    three = 0
    five = sugar // 5    # 큰 단위로 먼저 연산
    sugar %= 5           
    
    while five >= 0:
        if sugar % 3 == 0:
            three = sugar // 3    # // 몫 
            sugar = sugar % 3     # 3kg채우고 남은 설탕 양
            break
        
        five -= 1       # 3으로 연산 안될시 5 회귀
        sugar += 5
            
    return (three + five) if sugar == 0 else -1
        
print(count_sugar_box(sugar))