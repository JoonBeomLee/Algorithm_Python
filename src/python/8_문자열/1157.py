strs = input()
strs = strs.lower()
spells = [0] * 26

for i in strs:
    spells[ord(i) - 97] = spells[ord(i) - 97] + 1

order = sorted(spells)

count = 0
maxN = max(spells)

for i in spells:
    if(maxN == i): count += 1
        
if(count != 1): print("?")
else: print( chr(spells.index(maxN) + 97).upper() )