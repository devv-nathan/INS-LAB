import string 
import random

def gen_key():
    alphabet=list(string.ascii_uppercase)
    shuffled=alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet,shuffled))

def invert(keys):
    return{v:k for k,v in keys.items()}

def encrypt(text,key):
    cip=[]
    for ch in text:
        if ch.upper() in key:
            cip.append(key[ch.upper()])
        else:
            cip.append(ch)
    return "".join(cip)

def decrypt(text,key):
    cip=[]
    invertedkey=invert(key)
    for ch in text:
        if ch.upper() in invertedkey:
            cip.append(invertedkey[ch.upper()])
        else:
            cip.append(ch)
    return "".join(cip)

gen=gen_key()
print("Generated key is :\n",gen)

print("\nENCRYPTION")
t=input("Enter plaintext:\n")
e=encrypt(t,gen)
print("Encrypted text is : \n",e)

print("\nDECRYPTION")
d=decrypt(e,gen)
print("Decrypted test is :\n",d)
