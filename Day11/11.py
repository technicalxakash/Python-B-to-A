# num=2035
# if(num%4==0):
#     if num%400==0 or num%100!=0:
#         print("it is leap year")
#     else:
#         print("it is not leap year")
# else:
#     print(print("it is not leap year"))


#Loops
#Print 1 to N
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     print(i,end=" ")


#Sum of first N numbers
# n=5
# count=0

# for i in range(1,6):
#     count=count+i
# print(count)

#Factorial


# num=[5]
# factt=1
# for i in num:
#     factt=factt*i
#     i=i-1
# print(factt)

#Reverse a numbber
num = 123
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print(rev)


