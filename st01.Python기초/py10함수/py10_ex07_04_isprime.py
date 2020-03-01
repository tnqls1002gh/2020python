n = int(input("정수를 입력하시오: "))

def isprime(n):
    for i in range(2, n):
        if (n%i ==0):
            return False
        else: 
            return True

print(isprime(n))
