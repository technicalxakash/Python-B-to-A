#Sum of even numbers till N
n=6
cal=0
for i in range (2,n+1):
    if i%2==0:
        cal=cal+i
print(cal)
