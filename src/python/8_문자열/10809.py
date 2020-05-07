string = list(input())
spell = [-1] * 26

count = 0
for i in string:
    if(spell[(ord(i)-97)] == -1): 
        spell[ord(i) - 97] = count 
    count += 1    
        
for i in spell:
    print(i, end=" ")