#常用数据结构
# list_square=[]
# for i in range(1,4):
#     list_square.append(i**2)
# print(list_square)
#
#
# list_square2=[i**2 for i in range(1,4)]
# print(list_square2)
#
# list_square3=[]
# for i in range(1,4):
#     if i!=1:
#         list_square3.append(i**2)
# print(list_square3)
#
# list_square4=[i**2 for i in range(1,4) if i!=1]
# print(list_square4)

# list_square5=[]
# for i in range(1,4):
#     for j in range(1,4):
#         list_square5.append(i*j)
# print(list_square5)

list_square6=[i*j for i in range(1,4) for j in range(1,4)]
print(list_square6)

