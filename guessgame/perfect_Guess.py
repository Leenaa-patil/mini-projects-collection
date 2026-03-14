# geenrate a random number abd ask user to guess it. "higher number please"- guesss<number. "lowernumber please"- guess>number
import random
n=random.randint(1,100)

a=-1
guess=0
while (a!=n):
    
    a= int(input("whats your guess?"))
    
    if (a<n):
        print("higher number please")
        guess +=1
    elif(a>n) : 
        print("lower number please")
        guess +=1
  
print("yay!")
print(f"you guess the number {n} in {guess} attempts")    
