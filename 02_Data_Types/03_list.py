# List
#Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:

# List items are ordered, changeable, and allow duplicate values.

# The list is changeable:  add, and remove items in a list after it has been created.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "mango", "litchi"]
print(f'names of fruits in list: {(thislist)}')

print(f'the 0th orderd in list items: {thislist[0]}')
print(f'1st to 2nd: {thislist[1:3]}')       #1st include and last exclude
print(f'0th to 2nd {thislist[:2]}')

thislist[3] = "grapse"
print(thislist)

thislist[1:2] = ["cherry"] 
print(thislist)
print(thislist[1:3])

thislist[1:2] = ["banana", "litchi"]
print(thislist)

print(thislist[1:1])        #Empty
thislist[1:1] = ["test", "test"]
print(thislist)
thislist[1:3] = []          #remove both test
print(thislist)
print(len(thislist))

thislist = ['apple', 'banana', 'mango', 'litchi']
for fruits in thislist:
        print(fruits)
# for fruits in thislist:
        # print(thislist, end=",")
if "apple" in thislist:
        print("YES.apple is avaliable now")

if "cherry" not in thislist:
        print("NO.cherry is out of stok")
thislist.append("cherry")                      #use .append("item") for add items in list
print(f'check what in thislist, {(thislist)}')
if "cherry" in thislist:
        print("cherry here right now")

print(thislist.pop())                           #use .pop() for remove last item in list

print(f'check whatis inthislist {(thislist)}')

thislist.remove("mango")                        #use .remove("item") for remove whtaever you want in list
print(f'check what in thislist, {(thislist)}')

thislist.insert(2, "mango")
print(f'check what in thislist, {(thislist)}')  #use .insert(positon, "item") for add item in list

thislist_copy = thislist.copy()
print(thislist)                 #['apple', 'banana', 'mango', 'litchi']
print(thislist_copy)            #['apple', 'banana', 'mango', 'litchi']

thislist_copy.append("pomegranet")
print(thislist_copy)            #['apple', 'banana', 'mango', 'litchi', 'pomegranet']
print(thislist)                 ##['apple', 'banana', 'mango', 'litchi']

squared_num = [x**2 for x in range(10)]
print(squared_num)

cubed_num = [x**3 for x in range(6)]
print(cubed_num)


