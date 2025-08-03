#Dictionary

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

## Dictionaries are written with curly brackets, and have keys and values:

## Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

this_dict = {"brand" : "Ford", "model" : "Mustang"}
print(this_dict)

print(f'brand is :{this_dict["brand"]}')
print(f'model of car :{this_dict["model"]}')

print(this_dict.get("model"))

thisdict = {"brand" : "Dodge", "model" : "challenger", "color" : "black", "year" : "2008"}

print(f'model name:{thisdict["model"]}')
# print("kaifalifsiddique")
print(thisdict["brand"])

thisdict["year"] = "1970"           #change value
print(f'updated dic:{thisdict}')

for x in thisdict :                 #all value one by one, loop
    print(thisdict[x])

for x in thisdict : 
    print([x])                      #all key one by one, loop

for x in thisdict :                 #both key & value one by one,loop
    print(x,thisdict[x])            

for key, value in thisdict.items():
    print(key, value)

if "brand" in thisdict:             #if "key" in dictionary,,then print
    print("Yes")

print(len(thisdict))
print(len(this_dict))

this_dict["color"] = "Black"        #this_dict
print(this_dict)
print(len(this_dict))

this_dict.popitem()
print(this_dict)                    #remove last added item; .popitem()

thisdict.pop("year")                #remove- dict.pop("")  ; in thisdict
print(thisdict)                    

del this_dict["model"]
print(this_dict)

super_market = {
    "grocery" : {"masala" : "cumin", "oil" : "mustred"},
    "health" : {"dryfrutes" : "almonds", "milk":"amul"}
}

print(super_market)
print(super_market["grocery"])
print(super_market["grocery"]["oil"])

squared_num = {x:x**2 for x in range (7)}
print(squared_num)

squared_num.clear()
print(squared_num)