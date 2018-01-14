##Getting all prime numbers between two numbers using sieve of eratosthenes

def sieve(a, b):
    lyst = []
    for i in range(b+1):
        lyst.append(1)
    lyst[1] = 0 ##1 is not prime

    for j in range(2, b):
        for k in range(2*j, b+1, j):
            lyst[k] = 0

    for i in range(a, b+1):
        if lyst[i]:
            print(i, "is odd")

def main():
    START = 1
    END = 10
    sieve(START, END)

main()
    
