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

# num=371
# temp=num
# count=0
# total=0
# arm=0

# while(num>0):
#     last=num%10
#     count=count+1
#     num=num//10

# for i in str(temp):
#     arm=arm+int(i)**count

# print(arm)


#Prime number check

# num=10
# is_prime=True

# for i in range(2,(num//2)+1):
#     if(num%i==0):
#         is_prime=False
#         break

# if(is_prime==True):
#     print("it is a prime number")

# else:
#     print("it is not a prime number")


