#loops
#1)while
# i=1
# while i<10:
#     print(i)
#     i=i+1

# i=0
# while i<10:
#     print(i)
#     i+=1


# i=1
# while i<21:
#     print(i)
#     i+=2

# i=8
# while i>0:
#     print(f"the bus has seats {i}" )
#     i-=1
# print("all seats are booked")

# i=10
# while i>0:
#     print(i)
#     i-=1
# print("Happy new year")



# words=input("enter the sentence : ")

# results=""

# for ch in words:
#     if ch>="A" and ch<="Z":
#         results=results+ch.lower()
#     else:
#         results=results+ch.upper()
# print(results)



#for loop
# for i in range(1,11):
#     print(i)

# bag=["red", "greeen", "blue"]

# for baga in bag:
#     print(baga,end=" ") 

# name="akash"

# for index,i in enumerate(name):
#     print(f"{i} du index {index}")


# a={"A":"akash","B":"bag","C":"cat"}
# print(type(a))
# print(a.items())

# for i,j in a.items():
#     print(i,j)

# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{i}X{j}==={i*j}", end=",")
#     print()

# for i in range(1,31):
#     if(i%3==0):
#         print(i)
#     else:
#         continue


# res=0

# for i in range(1,11):
#     res=res+i
# print(res)
    


# char="akash"
# for i in char:
#     print(i , end=" ")
    

vow="this is my name"
count=0
for i in vow:
    if i=="a" or i=="e" or i=="o" or i=="u":
          count=count+1
    else:
         continue
print(count) 
