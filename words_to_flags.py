inp = input().lower()
rslt=[]
for ch in inp:
    if ch not in 'abcdefghijklmnopqrstuvwxyz':
        rslt.append(ch)
        continue
    rslt.append(chr(127365+ord(ch))) #this is a number and I'm not going to tell you how it was made
print(''.join(rslt))