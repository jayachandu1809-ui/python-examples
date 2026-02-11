'''n = int(input("enter no of rows:"))
for i in range (n):
   print(' '*(n-i-1)+'* '*(i+1))
for i in range (n-1):
   print(' '*(i+1)+'* '*(n-i-1))
   '''
 
'''for i in range(10):
   if i%2==0 :
      continue
   print(i)'''


s = 'ABCABCABCA'
subs=input('enter lettr:')
i = s.find(subs)
if i ==-1:
   print('not foind')
   while i !=-1:
      print('{} present at index:{}'.format(subs,i))
   i=s.find(subs,i+len(subs),len(s))   






         
   '''     print('*',end =' ')
    print()'''



   # print((chr(65+i)+' ')*n)





  # print('* '*n)
  # print(str(1+i)+ ' ')*n #
