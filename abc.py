#a=56
#if a==53 :
#       print 'a is even'
#elif a==57 : 
#      print 'a is odd number'
#elif a%2==0 :
#      print 'a is even number'
#a=6 
#if a>=0 :
#      print 'a is positive number'
#elif a==0 : 
#      print 'a is positve number'
#elif a <0 : 
#      print ' a is negative number'

a='546'
if type(a)==int: 
           a=float(a)    
           print a
elif  type(a)==float:
           a=str(a)
           print a
elif type(a)==str:
           print a
else: 
           print 'wrong data type'
