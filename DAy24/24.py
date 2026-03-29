#reverse a string in a sentence

strr="hi god how are you"
d=""
for i in strr.split():
    d=d+strr[::-1]+" "
    print(d)