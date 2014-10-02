import math

def isprime(number):
        if number<=1:
            return False
        if number==2:
            return True
        if number%2==0:
            return False
        for i in range(3,int(math.sqrt(number))+1):
            if number%i==0:
                return False
        return True

num=0
prime=0


while prime<10001:
    if isprime(num) == True:
        prime+=1
    num+=1

print(num, "is the 10001st prime")
