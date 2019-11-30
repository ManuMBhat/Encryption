import numpy as np
import math
import random
def isPrime(k):
    for i in range(2,math.ceil(k**0.5)):
        if not k%i:
            return False
    return True
def generateKeys(m=10):
    maxi = int("9"*m)
    mini = 10**(m-1)
    primes = [i for i in range(mini,maxi) if isPrime(i)]
    p = random.choice(primes)
    while True:
        q = random.choice(primes)
        if p!=q:
            break
    n = p*q
    phi = (p-1)*(q-1)
    for e in range(2,phi):
        if math.gcd(e,phi) == 1:
            break
    k = 1
    d = 0

    while True:
        r = k*phi + 1
        if r/e == r//e:
            d = r // e
            break
        k+=1

    return n,e,d

def EncryptMessage(publicKey,message):
    n,e = publicKey
    print(n)
    encrypted = ""
    for i in message:
        encrypted+= chr(pow(ord(i),e,n))
    return encrypted
def DecryptMessage(publicKey,privateKey,message):
    n,e = publicKey
    decrypted = ""
    for i in message:
        decrypted += chr(pow(ord(i),privateKey,n))
    return decrypted
def EncryptFile(publicKey,infilename,outfilename = "Encrypted.txt"):
    try:
        with open(infilename) as infile:
            with open(outfilename) as outfile:
                for line in infile:
                    outfile.write(EncryptMessage(publicKey,line))
        return True
    except:
        return False

     

def DecryptFile(publicKey,privateKey,infilename,outfilename = "Decrypted.txt"):
    try:
        with open(infilename) as infile:
            with open(outfilename) as outfile:
                for line in infile:
                    outfile.write(DecryptMessage(publicKey,privateKey,line))
        return True
    except:
        return False

        
if __name__=="__main__":
    n,e,d = generateKeys(2)
    print(n,e,d)
    message = "Test Message"
    Encrypted = EncryptMessage((n,e),message)
    print(Encrypted)
    print(DecryptMessage((n,e),d,Encrypted))