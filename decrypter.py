data = input('Enter the encrypted text (spaces apart of each number:')
encryptedtext = data.split()
keyremoved = []
alpha = 'abcdefghijklmnopqrstuvwxyz`1234567890-=[]\\;\'/.,'
finaltext = ''
textcounter = 0

with open('myprivatekey') as f:
    key = f.read()

for i in encryptedtext:
    temp = int(i) - int(key)
    keyremoved.append(temp)

print(keyremoved)

for i in keyremoved:
    temp = chr(i)
    finaltext = finaltext + temp

print(finaltext)

