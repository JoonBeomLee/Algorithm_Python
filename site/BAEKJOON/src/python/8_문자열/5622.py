dial = [" ", 
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'R', 'Q', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']
       ]

strs = input()
strs = list(strs)

sums = 0
for i in strs:
    count = 2
    for j in dial:
        if(i in j):sums = sums + count; break
        count += 1
            
print(sums)