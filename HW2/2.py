fizz = int(input())
buzz = int(input())
a = int(input())
b = 1
c = []
for i in range (1, a):
   if ((i % fizz == 0) and (i % buzz == 0)):
     print ("FB")
   elif (i % fizz == 0):
     print ("F")
   elif (i % buzz == 0):
     print ("B")
   else: print (str(i) )
