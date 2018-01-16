## Rishabh Dalal
## RSA encryption and decryption

from random import randint
import sys
import os

def l2int():
    myDict = {}
    for i in range(65, 91):
        myDict[chr(i)] = i-64
    return myDict

def sieve(a, b):
    ##Sieve of Eratosthenes
    
    lyst = []
    for i in range(b+1):
        lyst.append(1)
    lyst[1] = 0 ##1 is not prime

    for j in range(2, b):
        for k in range(2*j, b+1, j):
            lyst[k] = 0

    odd = []
    for i in range(a, b+1):
        if lyst[i]:
            odd.append(i)
    return odd

def gettingRandomNumber():
    ##Getting a large nmber to seed the primes number generator
    
    LENGTH = 10**5
    START = 10**3
    END = 10**4
    primes = sieve(START, END)
    return LENGTH + primes[randint(1, len(primes))-1]

def fermat(number):
    ##Checking to see if the number if prime acc to fermat theorem
    
    REPEAT = 5
    for i in range(REPEAT):
        base = randint(2, number-2)
        if not (base ** (number - 1))%number == 1:
            return False
    return True

def millerRabin(number):
    ##Checking to see if the number if prime acc to miller-rabin theorem
    
    newNumb = number - 1
    k = 0
    lastRes = 1

    while True:
        result = newNumb%(2**k)
        if result == 0:
            k += 1
        else:
            k -= 1
            m = (newNumb // (2 ** k))
            break
    a = randint(k, newNumb)

    return helper_miller(a, m, number)

def helper_miller(a, m, n):
    ##Helper method to faciliate the chain checking for miller-rabin algorithm
    
    comp = (a**m)%n
    count = 1
    if abs(comp) == 1:
        return True
    else:
        while True:
            new = (comp**2)%n
            if abs(new) == n-1:
                return True
            elif new == 1:
                return False
            comp = new
            count += 1

def secondaryTest(number):
    ##Testing the miller-rabin with many random bases to make sure number is
    ##prime
    
    TEST_TIMES = 5
    for i in range(TEST_TIMES):
        if millerRabin(number) == False:
            return False
    return True

def gettingE(n, phi):
    ##Getting the encryption key (from a list of all the possible keys for more
    ##randomisation)
    
    MORE_RANDOMISATION = 100
    lyst = []
    for i in range(2, phi):
        if (n%i):
            if (phi%i):
                lyst.append(i)
                if len(lyst) >= MORE_RANDOMISATION:
                    break

    return lyst[randint(1, len(lyst))-1]


def gettingD(E, phi):
    ##Getting the decryption key (using randomisation)
    ##randomisation)
    
    POSSIBLE_D = 2
    lyst = []
    for i in range(1, sys.maxsize):
        possibleD = (E*i)%phi
        if possibleD == 1:
            lyst.append(i)
            if len(lyst) > POSSIBLE_D:
                break
    
    print("D possible:", (lyst))
    return lyst[randint(1, len(lyst))-1]

def encrypt(mess, lock, secondKey):
    ##Ecrypting the message
    data = l2int()
    newMess = []
    for i in mess:
        newMess.append((data[i]**lock)%secondKey)
    return newMess

def decrypt(decr, key, secondKey):
    ##Decrypting the message
    
    oldMess = []
    for i in decr:
        oldMess.append((i**key)%secondKey)
    message = ""
    for i in oldMess:
        message += chr(i+64)
    return message


def main():
    
    message = input("Enter the message: ")
    SECOND_KEY = 14
    randNumber = gettingRandomNumber()
    if not randNumber%2:
        randNumber += 1

    prime1 = 0
    prime2 = 0
    count = 0
    for i in range(randNumber, randNumber**randNumber, 2):
        if fermat(i):
            if secondaryTest(i):
                if not count:
                    prime1 = i
                    count += 1
                else:
                    prime2 = i
                    break

    product = prime1*prime2
    coprimes = (prime1-1)*(prime2-1)
    print("Prime numbers generated", prime1, prime2)
    print("Phi", coprimes)
    encr_key = gettingE(product, coprimes)
    print("Encryption lock", encr_key)   
    encrypted_message = encrypt(message, encr_key, SECOND_KEY)

    decr_key = gettingD(encr_key, coprimes)
    print("Decryption key", decr_key)
    decrypted_message = decrypt(encrypted_message, decr_key, SECOND_KEY)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

main()
