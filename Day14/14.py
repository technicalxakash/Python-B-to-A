# number=8
# isprime = True
# for i in range(2,(number//2)+1):
#     if  number%i==0:
#         isprime = False
#         break

# if isprime == True:
#     print("it is a prime number")
# else:
#     print("it is a not prime number")
        


# for ii in range(2,11):
#     isprime = True
#     for i in range(2,(ii//2)+1):
#         if  ii%i==0:
#             isprime = False
#             break

#     if isprime==True:
#         print(ii)

#Fibonacci Series



# firstnumber=0
# secondnumber=1
# print(0)
# print(1)
# for i in range(1,10):
#     number=firstnumber+secondnumber
#     firstnumber=secondnumber
#     secondnumber=number
#     print(number)


#palindrome
word="racecar"
w1=""

for i in word:
    w1=i+w1
    

if w1==word:
    print("it is a palindrome")
else:
    print("it is not a palindrome")


