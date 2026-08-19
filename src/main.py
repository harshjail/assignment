import random 
g_no =  random.randint(1,50)
print("hello welcome to the number guessing game")
print(g_no)
num = int(input("Guess the number"))
while True:
   
    if num>g_no:
        print("number is very high")
    elif num<g_no:
        print("number is very less")
    else :
        print("hey finally you guessed the number correct hurrah")
        break
    num = int(input("guess again "))
    

