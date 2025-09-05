print("hello world") #parenthesis madhy lihycha string , case sensitive asti python
#variables  : memory location where data is stored ex name
name = "vaidehi"
age = 24
print(name) #value stored in name
print(age)
is_adult = True
#types of variables: string , integer , floating (point) , boolean (t or f)
name = "Tonny shark"
age = 51
is_genius = True
print (name)
print (is_genius)
#to take input from user use input variable
name = input("what is ur name? ")
print(name)

#concatination : joinging output with string or joining string with variable we use +
name = input("what is ur name ? ")
print("Hello " + name)

#ex
super_name = input("What is ur superhero name ? ")
print("my super hero name is  : " + super_name)

#type conversion
old_age = input("enter your old age : ")
int(old_age)
new_age = int(old_age) + 2
print(new_age)
number = 18
print(float(18))
print(bool(18))

#sum of two numbers (concatation)
first = input("enter first number : ")
second = input("enter second number : ")
sum = first + second
print(sum) #concatinate so o/p is 12

#sum of two numbers
first = input("enter first number : ")
second = input("enter second number : ")
sum = int(first) + int(second)
print(sum)

name = "Tony Stark"
print(name.upper())

#for searching
print(name.find('S'))
#returns index if not found returns -1
#indexing starts from 0
print(name.replace("Tony " , "Ironman "))
print(name)

#keywords are highlighted print , input
name = "Tony Stark"
print("Ironman" in name )    #find



#arithmetic Operator

print(5-2)

#// roundoff / point madhy yeata  % remainder operator  ** power

i = 5
i = i + 2
i += 2
i -= 2
i *= 2

#presedence rule

result = 2 + 3 / 5
print(result)

# comaprison operator - boolean operator define krtata
print(3 < 2)
print(3 <= 2)
print(3 != 3)  #notequal to !=


# logical operator or
print(2 > 3 or 2 > 1)

print(3 > 2 and 2 > 1)

print(not 2 > 3)  #opposite sangta

#if else statments

age = 2

if age >= 18:    #indendation is done in python space
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("your in school")
else:
    print("your a child")
print("thankyou")

#mini project

#range
numbers = range(5) # 0, 1, 2 , 3, 4,5
print(numbers)

#loops while (jab tak true tabtak true
i = 1
while i <=5:
    print(i)
    i = i + 1     #o/p 1,2,3,4,5
