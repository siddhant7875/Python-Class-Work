class Test:
    def add(self,a,b):
        res=a+b
        return res
    def sub (self,a,b):
        res=a-b
        print("the subtraction is",res)
        
a=int(input("Enter first number"))
b=int(input("enter second number")) 

T=Test()
answer=T.add (a,b)
print("The addition of two number are",answer)

T.sub(a,b)   