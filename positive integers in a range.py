# positive integers in a list 


list1 = []
 
n = int(input("Enter limit "))


 
 for i in range ( 0 , n ) :
   
 x = int( input())
  
  
  list1.append(x)
  
  
 print (x)
 
 
for num in list1:
     
    if num >= 0:
       print(num, end = " ")

