#reverse a string in a sentence

strr="hi god how are you"
d=""
for i in strr.split():
    d=d+i[::-1]+" "
print(d)


#find the sum of all ovules in the String
a="aeiouAEIOU"
buc=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        buc=buc+ord(i)
print(buc)    

a="qadehhio"

for i in a:
    if 