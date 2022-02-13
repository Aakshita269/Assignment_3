#QUESTION 1
#PROGRAM TO COUNT THE OCCURENCE OF EACH ALPHABET IN A GIVEN WORD ENTERED BY THE USER.          
print("QUESTION 1")

string=input("PLEASE ENTER YOUR OWN STRING:")
char=input("PLEASE ENTER YOUR OWN CHARACTER:")
i=0
count=0

while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1

print("THE TOTAL NUMBER OF TIMES",char,"HAS OCCURED=",count)

    
print("\n")
print("*" * 160)




#QUESTION 2
#PROGRAM TO GET NEXT DAY OF A GIVEN DATE.

print("QUESTION 2")

#TAKING INPUT OF YEAR FROM THE USER AND CHECKING IF ITS A LEAP YEAR OR NOT.
year=int(input("INPUT A YEAR:"))

if(year % 400==0):
    leap_year=True
elif(year % 100==0):
    leap_year=False
elif(year % 4==0):
    leap_year=True
else:
    leap_year=False


#TAKING INPUT OF MONTH FROM THE USER AND ALSO CHECKING HOW MANY DAYS WOULD IT HAVE.
month=int(input("INPUT A MONTH[1-12]:"))

if month in(1,3,5,7,8,10,12):
    month_length=31
elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
else:
    month_length=30


#TAKING INPUT OF DAY FROM THE USER.
day=int(input("INPUT A DAY[1-31]:"))

if day<month_length:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1
#PRINTING OUT THE NXT DATE FROM THE DATE ENTERED BY THE USER

print("THE NEXT DATE IS [YYYY/MM/DD] %d-%d-%d."%(year,month,day))

print("\n")
print("*" * 160)


#QUESTION 3
#PROGRAM TO CREATE A LIST OF TUPLES FROM A GIVEN LIST HAVING NUMBER AND ITS SQUARE IN EACH TUPLE

print("QUESTION 3")
#CREATING A LIST
list1=[2,5,4,8]

#USING LIST COMPREHENSION TO ITERATE EACH VALUE IN LIST AND CREATE A TUPLE
res=[(x,x**2) for x in list1]

#PRINT THE RESULT
print(res)



print("\n")
print("*" * 160)

#QUESTION 4
#PROGRAM TO PRINT GRADE AND PERFORMANCE BY TAKING AS INPUT THE GRADE POINTS BY THE USER.

print("QUESTION 4")

#TO MAKE A DICTIONARY FOR STORING THE STUDENTS' DETAILS
Dict={4:"Poor",5:"Below Average",6:"Average",7:"Good",8:"Very Good",9:"Excellent",10:"Outstanding"}
n=int(input("INPUT YOUR GRADE:"))

if(n<4):
    print("ERROR")
else:
    print("YOUR GRADE IS ",end="")
    print(n)
    print(" and ",end="")
    print(Dict.get(n),end=" Performance")


print("\n")
print("*" * 160)

#QUESTION 5
#PROGRAM TO PRINT TRIANGULAR PATTERN OF ALPHABETS.

print("QUESTION 5")

i=0
a="ABCDEFGHIJK"

#FOR HAVING ITERATIONS TO PRINT THE GIVEN PATTERN
for i in range(6):
    j=i
    while(j>0):
        print(" ",end="")
        j=j-1
    k=0
    for k in range(len(a)-2*i):
        print(a[k],end="")

    print("")
    

print("\n")
print("*" * 160)

#QUESTION 6
#PROGRAM TO PERFORM OPERATIONS ON DICTIONARY USED TO STORE STUDENTS' DETAILS.

print("QUESTION 6")

sid=int(input("ENTER YOUR SID:\n"))
name=input("ENTER NAME:\n")
students={sid:name}

while True:
    option=input("DO YOU WANT TO ENTER ANOTHER STUDENT ENTRY(Y or N):").upper()
    if option=="Y":
        sid=int(input("ENTER SID:"))
        name=input("ENTER NAME:")
        students[sid]=name
    elif option=="N":
        break
    else:
        print("INVALID INPUT!!")


#PART a
#TO PRINT THE DICTIONARY

print("<a>\n",students)

#PART b
#TO SORT THE STUDENTS' DETAILS ACCORDING TO THEIR NAMES

print("<b>\n",{k:v for k,v in sorted(students.items(),key=lambda x:x[1])})

#PART c
#TO SORT ACCORDING TO THEIR SIDs

print("<c\n",{k:v for k,v in sorted(students.items())})

#PART d
#TO SEARCH FOR A STUDENT BY THEIR SID

sid=int(input("SEARCH NAME WITH SID FOR:\n"))
print("<d>\n",students[sid])


print("\n")
print("*" * 160)

#QUESTION 7
#PROGRAM TO PRINT THE FIBONACCI SERIES AND PRINT THE AVERAGE OF THE RESULTANT SERIES.

print("QUESTION 7")
#TO PRINT A FIBONACCI SERIES FOR nterms ENTERED BY THE USER.
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

nterms=int(input("ENTER A NUMBER FOR THE NUMBER OF TERMS OF THE FIBONACCI SEQUENCE:"))


#CHECK IF THE NUMBER OF TERMS IS VALID.
if nterms<=0:
    print("PLEASE ENTER A POSITIVE INTEGER")
else:
    print("FIBONACCI SEQUENCE:")
    sum=0
    for i in range(nterms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/nterms)
print("AVERAGE OF THE RESULTANT FIBONACCI SERIES IS:",avg)
 

print("\n")
print("*" * 160)



#QUESTION 8
#PROGRAM TO PERFORM OPERATIONS ON GIVEN SETS OF NUMBERS.

print("QUESTION 8")

s1={1,2,3,4,5}
s2={2,4,6,8}
s3={1,5,9,13,17}


#PART a
#TO TAKE THE UNION,INTERSECTION AND THEN TO PERFORM THE GIVEN QUESTION
print("PART a")

Set_union=s1.union(s2)
Set_intersection=s1.intersection(s2)
a=Set_union-Set_intersection
print("<a>\n",a)


#PART b
#TO PRINT ELEMENTS THAT ARE ONLY IN ONE OF THE THREE SETS 
print("PART b")

b=s1.union(s2.union(s3))-s1.intersection(s2)-s2.intersection(s3)-s3.intersection(s1)
print("<b>\n",b)

#PART c
#TO SUBTRACT INTERSECTION OF THREE FROM TWO TAKEN AT ONE TIME
c=((s1.intersection(s2)).union((s1.intersection(s3)).union(s2.intersection(s3))))-s1.intersection(s2.intersection(s3))
print("<c>\n",c)

#PART d
#TO IGNORE THE NUMBERS FROM 1 TO 10 THAT ARE OCCURING IN s1

d=set()
for i in range(1,11):
    if i not in s1:
        d.add(i)
    print("<d>\n",d)

#PART e

e=set()
if i in range(1,11):
  if i not in s1 and i not in s2 and i not in s3:
    e.add(i)
print("<e>\n",e)

