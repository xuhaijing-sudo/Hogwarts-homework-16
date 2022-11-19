# f=open('data.txt')
# print(f.readable())
# #print(f.readlines()) #读出所有行
# print(f.readline())
# print(f.readline())
# f.close()
# with open('data.txt') as f:
#     print(f.readlines())

#图片读取需要使用rb 读取二进制格式
#正常的文本，可以使用rt，也就是默认格式
with open('data.txt') as f:
    while True:
        line=f.readline()
        if line:
            print(line)
        else:
            break



