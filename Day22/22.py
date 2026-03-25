
#count of vowels and consonents
strr="aakash  AAwAkash"
str=strr.lower()
count=0
count1=0
for ch in str:
    if ch==" ":
        continue
    elif ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count=count+1
    else:
        count1=count1+1

print(count)
print(count1)

#to find total numebr of Capital and smaller cases vowels
