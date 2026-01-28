#Tuple
"""
s=(1,2,3,4,5)
s1=(9,8,7,6,5,4)
s[0]=55
print(s)
#TypeError: 'tuple' object does not support item assignment

print(s[0:5:2])

print(s+s1)


#set
# s=set()
# print(type(s))
s11={1,2,3,4,5}
s22={55,12,5,6,7,8,9}
s11.add(10)

print(s11)

print(s11|s22)
print(s11&s22)
print(s11-s22)
s11.discard(10)

print(s11)
"""
s=[66,55,4,23,12,21,1,2,2,3,3,3,4,5,6,7,7,88,88]
print(s)
#tuple=tuple(s)
set=set(s)
print(set)