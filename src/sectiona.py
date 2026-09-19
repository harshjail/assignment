import random 
var =  random.randint(1,10)
print("guess the value between 1 and 10")
num = int(input("enter your guess:"))

if num == var:
    print("you guessed it correctly ")
else :
    print(f"you gueessed it wrong the correct values is {var}")
    
