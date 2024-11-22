#A dictionary is a built in data structure in python that allows you to store
#a collection of key value paris
#dictionary is mutable and it is unorderd

my_dict={
   "std_id":1233,
   "std_name":"siddhant",
   "course":"bca"
    }
print(my_dict)

#Accessing Elemnets

X=my_dict["course"]

print(X)

X=my_dict.get("std_name")

print(X)

#Get all the keys from specified dictionary
y=my_dict.keys()
print(y)

#to update particularcvalue

my_dict.update({"std_name":"simran"})
print(my_dict)

#adding items in the dictionary

my_dict["fees"]=45000
print(my_dict)

my_dict["std_add"]="navi mumbai"
print(my_dict)

#removing items in the dictionary using pop()

my_dict.popitem()
print(my_dict)

#looping over dictionary

for i in my_dict:
    print(i)
    
# looping over items in list
for i in my_dict:
    print(my_dict[i])

#looping by the method values() and keys()
print("use of values() method")
for i in my_dict.values():
    print(i)
    
print("use of keys() method")
for i in my_dict.keys():
    print(i)
    
#traversing dictionary
for x,y in my_dict.items():
    print(x,y)