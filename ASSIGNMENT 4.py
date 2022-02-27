#QUESTION 1
#RECURSIVE PYTHON FUNCTION TO SOLVE THE PROBLEM OF TOWER OF HANOI WITH THREE DISCS.
print("QUESTION 1")

def TowerofHanoi(n,from_rod,to_rod,middle_rod):
    if n==0:
        return
    TowerofHanoi(n-1,from_rod,middle_rod,to_rod)
    print("MOVE DISC",n,"FROM ROD",from_rod,"TO ROD",to_rod)
    TowerofHanoi(n-1,middle_rod,to_rod,from_rod)

#DRIVER CODE
n=3
TowerofHanoi(n,'A','B','C')    #A,B,C are the names of the rods

    
print("\n")
print("*" * 160)




#QUESTION 2
#TO PRINT THE PASCAL'S TRIANGLE FOR n NUMBER OF ROWS GIVEN BY THE USER USING BOTH RECURSIVE AND ITERATIVE PROCEDURES(FOR/WHILE LOOP)
print("QUESTION 2")
from math import factorial,remainder
from tracemalloc import start
n=int(input("ENTER THE SIZE OF THE PASCAL'S TRIANGE:"))

#USING FOR LOOP
print("USING FOR LOOP")

for i in range(n):
    for j in range(n-i+1):
        print(end=" ")     #FOR SPACING

    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")       #nCr=n!/((n-r)!*r!)
#FOR NEW LINE
    print()

#USING WHILE LOOP
print("USING WHILE LOOP")
i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i)//(factorial(y)*factorial(i-y)),end=" ")
        y+=1
    i+=1
    print()

#USING RECURSION
print("USING RECURSION")

def pas_triangle(n,originallength=n):
    if n==0:
        return
    pas_triangle(n-1,originallength)
    #TO PRINT THE SPACES
    print(" "*(originallength-n),end=" ")

#FIRST NUMBER IS ALWAYS 1
    start=1
    for i in range(1,n+1):

     print(start,end=" ")

#USING BINOMIAL COEFFICIENT
    start=start*(n-i)//i
    print()
pas_triangle(n)

print("\n")
print("*" * 160)


#QUESTION 3
#TO PERFORM OPERATIONS ON TWO NTEGERS INPUT BY THE USER AND PRINT THE QUOTIENT AND REMAINDER.

print("QUESTION 3")
int1,int2=map(int,input("ENTER 2 NUMBERS:").split())
Quotient=int1//int2
Remainder=int1%int2

#PART a
#TO CHECK WHETHER THE QUOTIENT AND REMAINDER IS A CALLABLE VALUE OR NOT.
print("a.) CHECKING IF THE QOUTIENT AND REMAINDER IS A CALLABLE VALUE OF NOT.")
print(callable(Quotient))
print(callable(Remainder))

#PART b
#TO CHECK FOR ZERO OR NON ZERO VALUES
if(Quotient==0):
    print("b.) THE QUOTIENT IS ZERO")
if(Remainder==0):
    print("b.) THE REMAINDER IS ZERO")
if(Quotient!=0 and Remainder!=0):
    print("b.) ALL THE VALUES ARE NON ZERO")

#PART c
partClist=[Quotient+4,Remainder+4,Quotient+5,Remainder+5,Quotient+6,Remainder+6]

result=[]
for i in range(len(partClist)):
    if partClist[i]>4:
        result.append(partClist[i])
print("c.) FILTERED OUT NUMBERS THAT ARE GREATER THAN 4 ARE:{result}")

#PART d
setresult=set(result)
print("d.) SET:",setresult)

#PART e
immutableSET=frozenset(setresult)    #FROZEN SET IS USED TO MAKE THE SET IMMUTABLE.
print("e.) IMMUTABLE SET;",immutableSET)

#PART f
print("f.) HASH VALUE OF THE MAX VALUE FROM THE ABOVE SET:",hash(max(immutableSET)))
print("\n")
print("*" * 160)

#QUESTION 4
#PROGRAM TO CREATE A CLASS NAMED STUDENT AND FILL IN DETAILS
print("QUESTION 4")

class Student:
    def __init__(self,student,roll_no):
         self.name=student
         self.roll_no=roll_no

    def __del__(self):
         print("OBJECT DESTROYED")

#CREATING OBJECT
student1=Student("AAKSHITA",21104005)
print("OBJECT CREATED")
#PRINTING THE ASSIGNED VALUES
print("THE NAME OF THE STUDENT IS {student1.name} AND SID IS {student1.roll_no}.")
#DELETING OBJECT
del student1


print("\n")
print("*" * 160)

#QUESTION 5
#PROGRAM TO CREATE A CLASS NAMED EMPLOYEE
print("QUESTION 5")
class Employee:
    def __init__(self,name,salary):
         self.name=name
         self.salary=salary

#CREATING EMPLOYEE RECORDS
employee1=Employee("MEHAK",40000)
employee2=Employee("ASHOK",50000)
employee3=Employee("VIREN",60000)

#PART a
#UPDATING SALARY
print("PART a")
employee1.salary=70000
print("THE UPDATED SALARY OF {employee1.name} IS {employee1.salary}")

#PART b
#DELETING A RECORD
print("PART b")
print("RECORD OF VIREN DELETED",end=" ")
del employee3
    

print("\n")
print("*" * 160)

#QUESTION 6
#PROGRAM TO ASSISST SO THAT THE TEST RUNS SMOOTHLY.
print("QUESTION 6")

#INPUTTING A WORD FROM THE FIRST FRIEND
word=input("ENTER THE WORD:")
word=word.lower()

#INPUTTING A MEANINGFUL WORD WITH THE EXACT SAME LETTERS
testword=input("ENTER A NEW MEANINGFUL WORD USING THE EXACT SAME LETTERS TO TEST YOUR FRIENDSHIP:")
testword=testword.lower()

#DEFINING DICTIONARY
def count_in_dict(word):
    count={}
    list1=list(word)

    n=len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]]+=1
        else:
             count[list1[i]]=1
    return count

#SHOPKEEPER'S INPUT TO VERIFY THE WORD'S MEANING
def userinput():
    if count_in_dict(word)!=count_in_dict(testword):
        print("THE LETTERS ARE NOT EXACT,FRIENDSHIP IS FAKE")
        return
    ans=input("DOES THE WORD MAKE SENSE?(Y/y or N/n)")

    if ans=="y" or ans=="Y":
        print("THE FRIENDS PASS THE FRIENDSHIP TEST")
    elif ans=="n" or ans=="N":
        print("THE WORD DOESN'T HAVE A MEANING,FRIENDSHIP IS FAKE")
    else:
        print("INVALID INPUT,TRY AGAIN WITH Y/y or N/n")
        userinput()
userinput()

print("\n")
print("*" * 160)

