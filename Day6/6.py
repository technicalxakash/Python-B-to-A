#Functions
#functions are resuable block of code that performs a specific task when called

# def h():
#     print("Hello good morining")

# h()


# def add(a,b):
#     print(a+b)

# add(1,2)



# l=[1,2,3,4,5,6]
# l.sort(reverse=True)
# g=l
# print(g)
#sort() modifies the original list and does not return the sorted list.

#sorted() returns a new sorted list without changing the original list.
# l=[1,2,3,4,5,6]

# g=sorted(l,reverse=True)
# print(g)


# def tables(num):
#     for i in range(1,11):
#         print(f"{num} X {i} = {num*i}")
#     print()
   

# tables(2) positional parameter
# tables(3)


# def tables(num=2): #default arugument
#     for i in range(1,11):
#         print(f"{num} X {i} = {num*i}")
#     print()

# tables()


#return=we are using the value in somewhere with the help of return

# def add(a):
#     #print((str(a))*5)
#     return int((str(a))*5)

# b=100

# c=b+add(2)
# print(c)
