t1=("siddhant","35","78","o grade")
print(type(t1))
print(t1)

#tuple slicing
print(t1[1:])
print(t1[:3])
print(t1[1:3])

#find lenght of the tuple

print("the lenght of the tuple is :",len(t1))

#you can also give negative indexing
print(t1[-2])
print(t1[-1])

#note
#list is a collection which is ordered and changeable
#list allows duplicate member
#tuple is a collection which is ordered and unchangeble
#tuple aloows duplicate members.

t2=list(t1)
print(t2)

t2[2]="a in sports"
print(t2)

#loop
for i in t2:
    print(i)