#Reverse number

# num=123
# rev=0


# while(num>0):
#     last=num%10
#     rev=rev*10+last
#     num=num//10
# print(rev)


#count number of digits

# num=123445
# count=0
# while num>0:
#     last=num%10
#     count=count+1
#     num=num//10
# print(count)


#Sum of digits

# num=12345
# sum=0

# while num>0:
#     last=num%10
#     sum=sum+last
#     num=num//10
# print(sum)


#largest number


# num=[1,2,3,44,3,23,45,200,100,120,99,180,210]
# largest=num[0]

# for i in num:
#     if i>largest:
#         largest=i
# print(largest)


#smallest number
# num=[1,2,3,44,3,23,45,200,100,120,99,180,210]
# samlest=num[0]

# for i in num:
#     if i<samlest:
#         samlest=i
# print(samlest)


#armstrong number

num=153
count=0
total=0
while(num>0):
    last=num%10
    count=count+1
    num=num//10
print(count)
