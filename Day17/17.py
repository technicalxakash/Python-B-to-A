# #Palindrome number
# num="racecar"

# # print(num[::-1])

# # new=""

# # for i in str(num):
# #     print(i,end="")
# numm=""

# for ch in num:
#     numm=ch+numm
# #print(numm,end="")



# if(num==numm):
#     print("it is a palindrome")
# else:
#     print("it is a not palindrome")


#Fibonacci N terms

# num=5
# first=0
# sec=1

# print(first)
# print(sec)
# while num>=0:
#     third=first+sec
#     first=sec
#     sec=third
#     num=num-1
#     print(third)


#Constructors
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def show(self):
#         print(f"{self.name} this dog age is {self.age}")

# dog1=Dog("scuby",6)

# dog1.show()


#wihtout Duplicates

# num=[1,2,3,4,5,6,78,6,2,3]

# uni=[]

# for i in num:
#     if i not in uni:
#         uni.append(i)
# print(uni)

# num=[1,2,3,4,5,6,78,6,2,3]

# uni=list(set(num))
# print(uni)


#print duplicate eleemnrs

# num=[1,2,3,4,5,6,78,6,2,3]

# dup=[]
# seen=[]

# for i in num:
#     if i in seen and i not in dup:
#         dup.append(i)
#     else:
#         seen.append(i)

# print(dup)


