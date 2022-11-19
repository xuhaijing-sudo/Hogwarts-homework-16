#json由字典和列表组成
import json
data={
    "name":["jerry",'nick'],
    "age":26,
    "gender":"female"
}
data1=json.dumps(data) #数据类型转换为字符串
print(data1)
print(type(data1))

data2=json.loads(data1) #字符串转换为json
print(data2)
print(type(data2))