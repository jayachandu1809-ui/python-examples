s = 'ABCABCABCA'
subs=input('enter lettr:')
i = s.find(subs)
if i ==-1:
   print('not foind')
while i !=-1:
   print('{} present at index:{}'.format(subs,i))
   i=s.find(subs,i+len(subs),len(s)) 