text = 'hello'
with open('myprivatekey') as f:
    key = f.read()

encryptedtext=[]

for i in text:
   encryptedtext.append(ord(i)+int(key))

print(encryptedtext)

