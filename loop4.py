n= int(input("which mutiplication table do you want between 2 to 6 "))
if 2<= n <=6:
    print(f"mutiplication table for {n}:")
    for i in range (1,11):
     print(f"{n} X {i} = {n*1}")
else:
    print("invalid input!")