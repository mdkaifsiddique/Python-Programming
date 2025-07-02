# Numbers: In Python, numbers are a fundamental data type used to represent numeric values.

# For examples- 
# Integers: 2,4,6,8, 5,3,etc
## Float- Decimal values
# octa - 0o; base 8
# hexa - 0x; base 16
# binary- 0b; base 2
# set()- empty set
num1 = 10
num2 = 20

# numeric operations: or Airithmic operations

#addition (+)
#add the two numbers:

result = num1+num2
print(f'the sum of the above two numbers is : {result}')


#substration
#sub the two numbers:

result = num1-num2
print(f'the difference of two num is : {result}')

# multiplication

result = num1*num2
print(f'the multiplication of two num is : {result}')

#division

result = num2/num1
print(f'the division of two num is : {result}')

#power
result = num1 ** 3
print(f'the power of 10^3 is : {result}')

# remainder
result  = num1 % 3
print(f'the remainder of 10/3 is : {result}')

(num1, num2)

#Decimal values
print(0.1+0.1+0.1) #0.3000000000000004
print(0.1+0.1+0.1-0.1)
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')) #0.2
# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal(0.3))

#boolian
True == 1 #True
False == 0 #False

# compare two values:(==){equal}
#                    (!=){not equal}

print(434.0==434.0) #True
print(435.0!=434.0) #True
print(5.0==4.00) #False
print('hello'=='world') #False

#floor - give bottom value
#trunc - give towards zero value

import math
print(math.floor(3.9)) #3
print(math.floor(-3.5)) #-4; -4 is less than -3.5
 
print(math.trunc(2.8)) #2
print(math.trunc(-2.7)) #-2; -2 is near to zero

print(0o10) #octal value is 8
print(0o20) #octal value is 16

print(f'the hexa value of 1 is {(0x10)}') #hexa value is 16
print(f'the hexa value of 2 is {(0x20)}') #hexa value is 32

print(f'the binary value of 1 is {(0b100)}')  #binary value is 4
# print(f'the binary value of 2 is {(0b200)}') #SyntaxError: invalid digit '2' in binary literal 

print (oct(64)) #convert int to oct, value is 0o100
print (hex(64)) #convert int to hex,
print (bin(64)) #convert int to bin,

print (int(3.14)) #3

print(f'the integer value 64 in octa {(int('64', 8))}') #connvert int to oct, int = 64, octa base is 8; result:52
print(f'the integer value 100 in binary {(int('100', 2))}') #connvert int to oct, int = 100, binary base is 2; result:4
print(f'the integer value 100 in hexa {(int('100', 16))}') #connvert int to hex, int = 100, hexa base is 2; result:256

import random
print(random.random()) #give the random number between 0 to 1
print(random.randint(1, 10)) #give the random number between 0 to 10

l1 = ['md', 'kaif', 'alif', 'siddique']
print(random.choice(l1))
print(random.shuffle(l1))
print(l1)                   

#set
setone = {1,2,3,4}
print(setone & {1, 3}) #intersection
print(setone & {1, 3}) #intersection
print(f'union of setone {setone | {1, 3, 7}}') #union
print(setone | {1, 3}) #union
print(setone - {1, 2, 3, 4}) 




