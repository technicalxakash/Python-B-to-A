#Largest Element in Array

# a=[1,2,3,4,66,5]


# max=a[0]

# for i in a:
#     if max<i:
#         max=i

# print(max)



#sec Largest Element in Array

# a=[1,2,3,4,66,5,8]


# max1=a[0]
# max2=a[1]

# for i in a:
#     if max1<i:
#         max2=max1
#         max1=i
#     elif max2<i and max2!=i:
#         max2=i

# print(max2)
# print(max1)


#Remove Duplicates

# a=[1,2,3,4,1,2]

# s=[]
# s=list(set(a))


# print(s)

#Remove Spaces

# a="a b c"

# b=a.split()

# nospace="".join(b)
# print(nospace)

# b=a.replace(" ","")
# print(b)


# a="listen"
# b="silent"


# sorted1="".join(sorted(a))
# sorted11="".join(sorted(b))

# if sorted1==sorted11:
#     print("it is an ana")


#Finding the duplicates
a=[1,1,2,2,3,3,4,5,6]

seen=set()
dup=set()

for i in a:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)

print(list(dup))