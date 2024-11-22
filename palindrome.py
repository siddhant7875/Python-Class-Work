n=int(input("Enter a number:"))
original = n
rev=0

while n> 0:
    rem = n% 10
    rev = rev * 10 + rem
    n = n // 10
    
print("the reverse is",rem)

if original == rev:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")
        