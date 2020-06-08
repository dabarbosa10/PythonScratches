from random import randint
success=0
attempts=10000
for ir in range (attempts):
    if randint(0,1)+randint(0,1)+randint(0,1)+randint(0,1)==3:
        success+=1
print("Number of attempts", attempts)
print("Number of success",success)
