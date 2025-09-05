#python properties 
#simple,east,opensource,highlevel language,developed by guido van rossum , portable same for diff os, backend django framework , web development , machine larning and many more 
""" if-elif-else
syntax: 
if(condition):
        statements1
elif(condition):
        statements2
else:
        statements3       
 """
light = input("Light : ")
if (light == "red" ):
    print("stop")
elif (light == "green"):
    print("go")
else:
    print("go slow")
    
    
    #nested loop
    """ if (condition):
            statement 1
            if (condition):
               statment2
            else:
                statment3"""
age = 95 
if(age >= 18):
  if(age >= 80):
       print("can  drive")
else:
    print("cannort drive")
    
#check given number is even or odd
    
num = int (input("number : "))
if(num % 2 == 0):
    print("EVEN")
else:
        print("ODD")
        
#list method - mutable asstata
#syntax list = [1,2,4]
""" list.append #adds  one element at the end 
list.sort = sorts list in ascending order 
list.sort( reverse=True) sorts list in descending order
list revers() #reverses  list 
list indsert(idx,el) = inserts elements at index
list.remove(1) = removes first occurance of element 
list.pop(idx) = removes element at idx """

#tuple - builtindata type lets us create immutable sequence of values "cannot change"
#syntax tuple =(2,1,4)
""" methods in tuple 
tup.index(el) #returns index first occurance 
tup.count(el) #counts  total occurance """

list1 = ["m","a","a","m"]
copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrom")
    
#sort in ascending order
grade = ["a","b","d","c","a"]
grade.sort()
print(grade)

#dictionary store data in value in key:values 

dict = {
    "name" : "vaidu",
    "cgpa" : "9.00",
}
print(dict)