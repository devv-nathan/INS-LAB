keys={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}

def encrypt(text):
    text=str(text)
    encrypting=[]
    for l in text:
        encrypting.append(keys.get(l,l))
    print(''.join(encrypting))
    
def decipher(text):
    text=str(text)
    decrypted=[]
    for l in text:
        decrypted.append(keys.get(l,l))
    print(''.join(decrypted))
    
print(encrypt("hello world"))
print(decipher("svool dliow"))
