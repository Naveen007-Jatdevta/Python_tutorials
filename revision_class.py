
"""
DISCUSSION:
0. Make variable
1. Printing statements
2. data types
3. Type casting.
    - user input()
    
4. Always take care about intendation.
5. comments can be added using #,""" """". 
6. commented statement isn't executed by the programing language.
"""


#variable:
my_var = 12

a = 20

c = "hello"

d = True



# Print
"""
When to use: 

- printing the variable values.
- printing the sentences.
- printing debugging.

"""

# a = " Bye people!!!!!"

# print( a )






# TAKE USER INPUT:

# - Hardcoding
# - Duynamic

# a = 12  # haercoded

# b = input("Please enter value: ") # dynamic

# print("Value is: ",b)





# TYPE-CASTING:
    # - finding the datatype of the varaible.
    # - casting the varaible datatype.
    # - understanding input().


# int - 12, 45, 99999999999
# float - 12.54, 67.85757
# str - "12", "hebuybuf", 'hey'
# bool - True / False , 1/0, High/Low


# 1. type() -> for finding datatypes of the variable.

# a = '123'
# b = type(a)
# print(b)

# a = 12.98
# b = str(int(a))
# print("type is: ",type(b))

# print("original:", a)

# b = str(a) # float -> int

# print("After type casting: ",b)


# calculator


# Hardcoding
# a = 10
# b = 20

# print(a+b)


# Dynamic
# a  = int( float( input("Enter value a; ") ))
# b = int(float(input('Enter value b: ')))

# print(a+b)


# add = +
# sub = -
# multi = *
# division = /



# s1 = '10'
# a = int(s1)

# s2 = '20'
# b = int(s2)

# print(a+b) 




"""
Q1. typecaste hardcoded(Progammer feeded) value into:
	- int
	- float
	- string
	The value is -> 49, 49.67, "Tom Cruise"
"""

###################################




# datatype:
# 1. int -> 1, 23, 44, 100, 199, 9999999999
# 2. float -> 2.3 33.6, 9999.0, 2.0
# 3. str -> "hello" or 'hello    -> "23" / ''\
# 4. boolean -> bool -> True/ False true= 1, false =0


# a = rajat
# print(a)









"""
Q1. typecaste hardcoded(Progammer feeded) value into:
	- int
	- float
	- string
	The value is -> 49, 49.67, "Tom Cruise"
"""

# a = '12'
# print(a)

# fetch_data  =  12.55

# print(type(fetch_data))


# a = '1223'

# print(type(a))

# b = float(a)  
# print(b)

# c = int(b)
# print(c)

# print(type(c))





# typecast float -> float
# print(float(a))

# typcaste float -> int
# print(int(a))

# typecaste int to string
# print(str(a))

# typecaste str to int


##### input statement #####


# enter your age, add 2 years in user's age and print it


# a = int( float(   input(" bhaiya enter your age: ")   ) )
# print('bhaiaya ur age is: ', a)

# sum = a+2*21/2

# print('new age is: ', sum)


# a = 12
# sum = a + 2
# print(sum)





###############
### IF LOOP ###
###############

"""
DISCUSSIONS:
1. structure of if else condition is 'if' and ends with 'else' 
elif always comes in between. 
"""



#comaprison operators:
# <
# >
# >=
# <=
# =  -> assignment operator
#  == -> comparison
# and -> T T -> T











# age = int(input("Enter your age:  "))


# if else condition

# if (age >= 18):

#     print('Adult')

# elif   (16<=age<=18):

#     print('He is idot')
    
# elif( 12<age<16):

#     print('paagal')

# else:
#     print('Kid')



















# if (condition):
    
# 	print('write asny code')

# elif (condition):

# 	print('write asny code')

# elif (condition):

# 	print('write asny code')
# elif (condition):

# 	print('write asny code')

# else:
# 	print('write asny code')


# MATHEMATICAL OPERTAORS:
# + - / * **

# COMPARISON OPERATORS: 
# > < >= <= ==

# =    OR     ==

# a = 12

# a == 14


"""
Q3. Accept any city name from the user and display the monuments 
of the city name:
 - if city is delhi then print monument red fort
 - if city is Agra then print monument Taj Mahal
 - if city is Jaipur then print monument Jal Mahal
"""

# city = input('Enter city: ')

# if city == 'delhi':
#     print('red fort')
    

# elif (city == 'Agra' ):
# 	print('Taj Mahal')
        

# elif (city == 'Jaipur'):
#       print('Jal Mahal')

# else:
#       print('None')


"""
Q3. Accept any city name from the user and display the monuments 
of the city name:
 - if city is delhi then print monument red fort
 - if city is Agra then print monument Taj Mahal
 - if city is Jaipur then print monument Jal Mahal
"""


"""
Q5. Write a python program for assigning grades 
(A, B, C, D, E, F, G) based on marks obtained by a student.
	- if the percentage is above 95, assign grade A
	- if the percentage is above 70 and below and including 95, assign grade B
	- if the percentage is above 60 and below and including 70, assign grade C	
    - if the percentage is between (50, 60), assign D
    - if the percentage is (40 to 50), assign E
    - if the percentage is 29 and 30 , assign F
    - if the percentage is 10 or 11, assign G 
"""


# per = int(input('Enter you marks: '))
# # per2 = int(input('Enter you marks: '))

# if (per > 95):
#     print('A')

# elif ( 70<per<=95):
#     print('B')

# elif(60<per<=70):
#     print('C')

# elif (50<per<60):
#     print('D')

# elif(40<=per<=50):
#     print('E')

# elif (per==29) and (per == 30):
#     print('F')

# elif (per==10) or (per ==11):
#     print('G')


# else:
#     print('No grades')



"""
Q9: Write a python program, A shop will give discount of 10% 
    - if the cost of purchased quantity is more than 1000 bucks. 
Also,
- Ask user for quantity [Suppose, one unit will cost 100 bucks].
- Judge and print total cost for user.
"""



"""
Q10: Write python program to accept the electric units from user 
and calculate the bill according to the following criteria:

First 100 units is Free

next 200 units is Rs 2 per unit

Above 300 units is Rs 5 per unit
"""
 


# unit =  int(input("Enter your electric units: "))

# amount = 0

# if (unit <= 100):
#     amount = 0 
#     print('Your amount is: ', amount)

# elif (100 < unit <= 300):

#     amount = 0 + (unit-100) * 2
#     print('Your amount is: ', amount)

# else:

#     amount= 0 + 200*2 + (unit-300) * 5
#     print('Your amount is: ', amount)













"""
Q5. Write a python program for assigning grades 
(A, B, C, D, E, F, G) based on marks obtained by a student.
	- if the percentage is above 95, assign grade A
	- if the percentage is above 70 and below and including 95, assign grade B
	- if the percentage is above 60 and below and including 70, assign grade C	
    - if the percentage is between (50, 60), assign D
    - if the percentage is (40 to 50), assign E
    - if the percentage is 29 and 30 , assign F
    - if the percentage is 10 or 11, assign G 
"""

# marks = int(float(input("Enter marks: ")))
# # marks2 = int(float(input("Enter marks: ")))
# if (marks > 95):
#     print('A')

# elif (  70 < marks <= 95):
#     print('B')

# elif (60 < marks <= 70):
#     print('C')

# elif (50 < marks < 60):
#     print('D')

# elif (40 <= marks <= 50):
#     print('E')

# elif (marks==29 or marks==30):
#     print('F')
    
# elif (marks==10 or marks==11):
#     print('G')










"""
Q6: Write python program that ask two user input and find largest 
number out of that two user input number.
"""

# a = int(float(input("Enter value: ")))

# b = int(float(input("Enter value: ")))

# if a>b:
#     print('a')

# elif b>a:
#     print('b')

# else:
#     print('a = b')


"""
Q7: Write python program that accepts age of 4 users and find the
youngest user out  of it.
"""

# a = int(float(input("Enter value: ")))

# b = int(float(input("Enter value: ")))

# c = int(float(input("Enter value: ")))

# d = int(float(input("Enter value: ")))


# if (a < b and a < c and a < d):
#     print('a is youngest')


# elif (b < a and b < c and b < d):
#     print('b is youngest')


# elif (c < a and c < b and c < d):
#     print('c is youngest')


# elif (d < a and d < b and d < c):
#     print('d is youngest')



"""
Q8: Write a python program to find the area of the:
    - Rectangle
    - Circle
    - Triangle
    - Square
"""

# shape  =input("Shape: ")

# if shape == 'rectangle':
    
#     length = int(float(input("Enter length: ")))
#     breadth = int(float(input("Enter breadth: ")))
#     area = length * breadth
#     print(area)
    



"""
Q9: Write a python program, A shop will give discount of 10% 
    - if the cost of purchased quantity is more than 1000 bucks. 
Also,
- Ask user for quantity [Suppose, one unit will cost 100 bucks].
- Judge and print total cost for user.
"""





# # printing ways:
# # 1.
# a = 10
# b = 20
# print('hello', a)

# # 2.
# print(f'hello {a}')

# # 3.
# print('hello {} {}'.format(b, a))




"""
Q10: Write python program to accept the electric units from user 
and calculate the bill according to the following criteria:

First 100 units is Free

next 200 units is Rs 2 per unit

Above 300 units is Rs 5 per unit
"""


# units = float(input('Enter unit: '))

# amount = 0

# if ( 0 < units  <= 100):

#     print(f'user needs to pay {amount}')


# elif ( 100 < units <= 300 ):
    
#     amount = 2 * (units-100)
#     print(f'user needs to pay {amount}')


# else:

#     amount = (0) + (200*2) + (units-300) * 5

#     print(f'user needs to pay {amount}')




################
### FOR LOOP ###
################

"""
DISCUSSION:
1. For loop
    - Iteration -> no.of times to loop 
    - Index -> Location

2. range() funtion
"""











"""
Q11. Print first 10 natural number.
"""


# print(1,2,3,4,5,6,7,8,9,10)

# print(1)
# print(2)
# print("...", end='\n')
# print(10)


# for i in range(1, 11):
#     print(i)

# print('last i is: ',i)


"""
Q12. Print numbers from -10 to -1 using for loop.
"""

# for i in range(-10, 0,  1):

#     print(i)





"""
Q13. make variables for start and end points for looping and 
printing the values.
"""

# start = 1
# end = 11
# jump = 1

# for i in range(1, 11, -1):

#     print(i)




"""_
Q find the sum of first 10 numbers:
"""

# print(0+1+2+3+4+5+6+7+8+9)

# sum = 0
# for i in range(10):
    
#     sum = sum + i

# print(sum)





"""
DISCUSSIONS:
1. List 

2. List built-in methods:

    1. append() - add in end
    2. insert() - specify location
    3. remove() - specify element name
    4. pop()    - use index
    5. slicing [:] - print ample of specified contained at once.
    6. len()    - find length of the list
    7. index()  - to find index of specific element and even specify limit till which u want to find
    8. sort()   - sort element in ascending order.

"""

# 1
# a = [[ 1, 2, 'max', 12] ,  [1,2] ]


# 2

# a = list( (1, 234, 4) )
# print(a)

#  LIST OPERATIONS:

# a = [1,23,45, 12, 100 , 22 ,23333]

# for i in reversed(a):
#     print(i)

# a.reverse()

# print(a[::-1])]



# a.append( 1000 )

# a.insert(3, 'hellllllooooo')

# a.remove( 'mas' )
# a.pop(4)


# b =  a[1 : 5]
# print(b)

# print( len(a) )

# a.sort()

# print(a)

# print(a[ : : -1])





"""
Q16. Write python program that accepts age of 4 users and find the
youngest user out of it.
"""

# mlist = []

# for i in range(4):
    
#     a = int(input('enter age:' ))
    
#     mlist.append(a)

# print(mlist)

# # sorting the list

# mlist.sort()


# print('sorted list: ',mlist)

# print('youngest person age is: ', mlist[0] )




"""
DISCUSSIONS:
1. break, pass, continue 
2. Backtracing in list
    - reversed()
    - a.reverse()
    - a[: : -1]
"""

"""
BREAK - COMES OUT OF THE LOOP
PASS  - DOES NOTHING
CONTINUE - SKIPS THE ITERATIONS
"""

# a = [12, 10, 23, 34, 55, 12]

# for i in a:

#     if i >= 20:

#         break

#     else:
#         print(i)




"""
Q.1 Consider the situation where you need to write a program that 
prints the number from 1 to 10 but not 6.
"""


# for i in range(1, 11):


#     if i == 6:
#         continue

#     print(i)





"""
Q1. Write a program to print the cube of all numbers from 1 
to a user input numbers.
"""

# HOMEWORK











""" OBJECTIVE:

1. String operations
2. What is whitespace
"""




# mlist = [1,23,44,23]
# mstr = "hello world"  #-> ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '%']


"""
1. concatinate operation ( + ) -> merge 
"""


# # a = '2' + '3'
# # print(a)


# a = input('Enter string 1: ')

# b = input('Enter string 2: ')

# # concatinate:
# c = a + b

# print(c)






# a = int(input('Enter value'))
# b = int(input('Enter value'))
# c = a+b 

# a = 's'
# b = 'd'

# c = "c"
# print( c )


# c = " c"
# print( c )


# c = "   c"
# print( c )



"""
2. multiply the string ( * )
"""

# a = 2  
# b = 5

# c = str(a) * b

# print(c)




# a = "*"

# print( a * 10)










"""
3. string slicing
"""

# # list
# m = [1, 2, 34, 32, 22]

# b = m[ 1: 3 ]
# print(b)

# # string
# a =  'hello world!! bye word!!'

# b = a[ 3 : 7 ]
# print(b)











"""
4. case changing ( upper(), lower() )
"""

# a = ' HELLO WORLD !!'

# b = ' bye.....'

# print(b[3].upper())


# # print( a[1: 5] + b )






"""
5. white space removal  ( stip() )  removes element from 
    leading and ending.
"""


# a = "   .,,,,,rrttgg.....banana....rrr,,,||,y,,,e,  "


# # print(a)


# print(a.strip(",e .|rr"))



# print(a, '\n')

# print( a.strip('|,.r') )



# b = a.strip(",r.")
# print(b)


"""
6. splitting the string ( split() )  -> split the string n form list
"""

# a = ' Helloworld!!!! my bye '

# print( a.split() )




"""
7. looping the string
"""

# a = 'hello'

# for i in a:

#     print(i , end=" " )




"""
8. replacing the element in the string. (replace())
"""

# a  = ' Hello!!!!!  world  '

# print(a)


# replace( "old_value", "new_value")
# print(a.replace('  ', "*"))





# print(a.replace('!!!!!', ' '))

"""
7. join function:
"""

# a = 'hello people,'

# b = ' walla!!!'

# print(a+b)


# connector = ' '
# b ='hello people, walla!!!'
# print(b.split())
# # print(a+b)

# c = connector.join(b)
# print(c)