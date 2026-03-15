#Reverse a string and explain the code.

# strr="akash"
# print(strr[::-1])

# strrr="madamm"
# a=""
# for i in strrr:
#     a=i+a
# print(a)


#Write a palindrome program.

# num="madam"
# rev=""
# for i in str(num):
#     rev=i+rev
# print(rev)

# if num==rev:
#     print("it is a palindrome")

# else:
#     print("it is not plaindrome")


#Write a Fibonacci Series



# firstnum=0
# secondnum=1


# for i in range(0,10):
#     print(firstnum)
#     temp=firstnum+secondnum
#     firstnum=secondnum
#     secondnum=temp

#swap of a numebr

# a=2
# b=3

# temp=a
# a=b
# b=temp

# print(a)
# print(b)


#fact

# num=5
# sum=1

# for i in range(1,num+1):
#     sum=sum*i
# print(sum)


#using recursion
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))

#Prime Number Program


# num=8
# is_prime=True

# for i in range(2,(num//2)+1):
#     if num%i==0:
#         is_prime=False
#         break


# if(is_prime==True):
#     print("it is prime")
# else:
#     print("it is not a prime")


# num=11
# for i in range(2,num):
#     if(num%i==0):
#         print("not a prime")
#         break
# else:
#     print("it is a prime")



# def func(num):
#     for num in range(1,51):
#         if(num>1):
#             is_prime=True
    

            

#             for i in range(2,(num//2)+1):
#                 if num%i==0:
#                     is_prime=False
#                     break


#             if(is_prime==True):
#                 print(num)

# print(func(6))


#Reverse a number

# num=1211

# a=""

# for i in str(num):
#     a=i+a
# print(int(a))


#prime number

# def bool(num):
#         for num in range(1,num+1):
#            if num>1:
#             is_prime=True

#             for i in range(2,(num//2)+1):
#                 if(num%i==0):
#                     is_prime=False
#                     break;
#             if(is_prime==True):
#                     print(num)

# bool(10)