i = 1
while i <=2:
    print(i)
    i = i + 1

#pattern printing

i = 1
while i <=5:
    print(i * "*")    #*multiply sting also possible
    i = i + 1

i = 5
while i >= 0:

    print(i * "*")
    i = i - 1

#for keyword in keyword

for i in range(5):
    print(i)

#for loop
for item in range(5):
    print(item + 1)

#list datatypes : collection of items
marks = [95,98,97]
print(marks)
print(marks[0])   #index can be -ve - means from back countig
print(marks[-1])
print(marks[0:2])
print(marks[1:3])

for score in marks:
    print(score)

    #append operation joining
marks.append(99)
print(marks)

marks.insert(0,56) #insert use for inserting at particular index ( index , value)
print(marks)

print(99 in marks) #checking 99 aheaka tya sathi in keyword use krto
print(93 in marks)
print(len(marks)) #len of list

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

#empty list clears the list
marks.clear()
print(marks)

#break and continue


students = ["ram", "Sham" , "mona" , "radha"]

for student in students:
    print(student)

#list denoted by []
students = ["ram", "Sham" , "mona" , "radha"]

for student in students:
    if student == "mona" :
        break;
    print(student)

#continue tevha vaparnr jr ty soodun bakichy havy asstil tr
students = ["ram", "Sham" , "mona" , "radha"]

for student in students:
    if student == "Sham":
        continue;
    print(student)

#structure : tuple list srkhch fkta imutable cant be change later denoted ()
marks = (95,98,97)

#tuple can count how much time came
print(marks.count(97))
print(marks.index(97))


#structure : set - collection of unique elements  represented by {}
marks = { 95, 98 , 97, 97 ,97}

for Score in marks:
    print(Score)

    #structure : dictionary - key:value pairs stored eg : student  : list , tuple

    marks = {"english" : 95 , "chem" : 98 }
    print(marks["chem"])

    marks["physics" ] = 97 ;
    print(marks)

    marks["physics"] = 99;
    print(marks)


#functions 1.In-built function : aready asstat  int() str() bool()
#          2. Module functions : related fuctions or variable ek thikani thevto tyala module boltat eg : math module
import math
print(dir(math))
from math import sqrt
print(sqrt(4))

#*used for select all
#          3. user defined functions

#def function_name(parameters):

#    //do something

def print_sum(first ,  second):
    print(first + second)
print_sum(1,2)


def print_sum(first , second=4):
    print(first + second)

print_sum(1)