import os
import time
# # os.mkdir("testdir")
# os.listdir("./")
# os.removedirs("testdir")

print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f=open("b/test.txt", "w")
    f.write("hello,os using")
    f.close()

print(time.asctime())
print(time.time())
print(time.localtime())


