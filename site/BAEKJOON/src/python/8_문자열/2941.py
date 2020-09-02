alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

strs = input()

for i in alpa:
    if(i in strs):
        strs=strs.replace(i, "_")

print(len(strs))