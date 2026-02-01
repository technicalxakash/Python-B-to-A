#exception Handling
# try:
#     a=100
#     b=20
#     c=0
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/c)
#     print(b/a)
#     print(a/b)
# except ZeroDivisionError:
#     print("c should be not be 0 ")

#after error it will excecute the next lines so i am using the functions





# a=100
# b=20
# c=0

# def siz(a,b,c):
#     try:
#         print(a/b)
        
#     except Exception as e:
#         print(f"error : {e}")
#     try:
        
#         print(a/c)
#     except Exception as e:
#         print(f"error : {e}")

# print(a+b)
# print(a-b)
# print(a*b)

# siz(a,b,c)


# if __name__ == '__main__':
#     n = int(raw_input())
#     integer_list = map(int, raw_input().split())
#     a=tuple(integer_list)
#     print(hash(a))

# ABCDCDC
# CDC

str11="ABCDCDC"
str1="CDC"
for i in str11:
    print(str11[3])
