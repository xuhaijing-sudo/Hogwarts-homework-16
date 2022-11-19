#元祖的定义
# tuple_hogwarts=[1,2,3]
# tuple_hogwarts2=1,2,3
# print("tuple_hogwarts",tuple_hogwarts)
# print("tuple_hogwarts2",tuple_hogwarts2)
# print(type(tuple_hogwarts))
# print(type(tuple_hogwarts2))

#元祖的不可变特性
# list_hogwarts=[1,2,3]
# list_hogwarts[0]="a"
# print(list_hogwarts)

# a=[1,2,3]
# tuple_hogwarts=(1,2,a)
# tuple_hogwarts[2][0]="a"
# print(tuple_hogwarts)


# a=(1,2,3,"a","a","a")
# print(a.count("a"))
# print(a.index(3))


#集合
# a={1,2,3}
# b={1,4,5}
# print(a.union(b))
# print(a.intersection(b)) #求交集
# print(a.difference(b))#求差集
# a.add("a")
# print(a)


#字典的key值不可变
# c="asasbnasa"
# print(set(c))
# hogwarts_dict={"a":1,"b":2}
# hogwarts_dict2=dict(a=1,b=2)
# print(hogwarts_dict)
# print(hogwarts_dict2)

# a={"a":1,"b":2}
# print(a.keys())
# print(a.values())
# print(a.pop("a"))
# print(a)

# a={"a":1,"b":2}
# #返回被删除的键值对
# print(a.popitem())
# #删除掉上面执行的键值对后，还剩余的键值对
# print(a)

a={}
b=a.fromkeys((1,2,3),"a")
print(b)

print({i:i**2 for i in range(1,3)})