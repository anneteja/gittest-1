n1=int(raw_input("enter 1st num"))
n2=int(raw_input("enter 2nd num"))
n3=int(raw_input("enter 3rd num"))
if   (n1>n2) and (n1>n3):
         largest=n1
elif  (n2>n1) and (n2>n3):
         largest=n2
else:
   largest=n3
print("The largest number between",n1,",",n2,"and",n3,"is",largest)
