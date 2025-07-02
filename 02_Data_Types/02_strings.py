# Strings
#Strings in python are surrounded by either single quotation marks, or double quotation marks.

# for example 'hello' is the same as "hello"
print('Hello world')
print("Python launguage is similar to 'English'")

# Assign String to a Variable

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

alif = "Hello world"
print(alif)

first_char = alif[0]
print(first_char)       # H

l1 = alif[6]
print(l1)               # w

slice_alif = alif[0:9]
print(slice_alif)       #Hello wor
print(alif[-1])         #d

num_list = "0123456789"
print(num_list[:])

print(f'numbers above the four {(num_list[4:])}')
print(f'numbers below the nine {(num_list[:9])}')
print(f'hopping {(num_list[0:7:2])}')

print(alif)

print(f'uppercase {(alif.upper())}')
print(f'lowercase {(alif.lower())}')

alif = "   kaifalif   "
print(alif)
print(alif.strip())     #strip: remove extra spaces

alif = "mr alif"
print(alif.replace("mr", "Kaif"))

alif = "Md, Kaif, Alif, Siddique"
print(alif.split(", "))

alif = "Hello World"
print(f'find what position to world in Hello World {(alif.find("World"))}')

print(alif.find("world"))  #result is -1;-1 means it not found world in Hello World.
alif = "Hello World World World World"
print(alif.count("World"))  #for counting how many time World in Hello World

alif_type = "Chai"
quantity = 3 
order = "I ordered {} cups of {} "
print(order.format(quantity, alif_type))

name_variety = ["Kaif", "alif", "siddique"]
print("".join(name_variety)) #change list to string

print(" ".join(name_variety))
print("-".join(name_variety))  #Whatever you want between["Kaif", "alif", "siddique"] write it in between (""); as"-" |","etc

alif = "Hello World"
print(f'the length of in Hello World is: {(len(alif))}')

for letter in alif:
        print(letter)

alif = "He said, \"Python is very useful\" "
print(alif)

alif = 'Kaif\nalif'
print(alif)

alif = r"c:\\user\\python\\"
print(alif)
alif = r"c:\user\python"
print(alif)

alif = "alif statistics"
print("statistics" in alif)     #True
print("Statistics" in alif)     #False

if "statistics" in alif:
        print("Yes,'statistics' is present")
        print("Yes,'Statistics' is present")
        print("Yes,'kaif' is present")

