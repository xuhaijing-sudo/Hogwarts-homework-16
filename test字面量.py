# name='hogwarts'
# age=3
# print('my name is %s'%name,'my age is %d'%age)
# print('my name is %s,my age is %d'%(name,age))
# print('my name is {},age is {}'.format(name,age))

# name='lili'
# age=20
# list1=[1,3,4]
# dic1={'name':'tom','gender':'name'}
# print('my list is {},dict is {}'.format(list1,dic1))
# print('my name is {1},age is {0},{0}{1}{1}'.format(name,age))
#
# namelist = ['lili','tom','jerry']
# print('we are :{},{} and {}'.format(*namelist))
#
# print('my name is {name},gender is {gender}'.format(**dic1)) #字典解包

name='lili'
age=20
list1=[1,3,4]
dic1={'name':'tom','gender':'male'}
print(f"my name is {name},age is {age}")
print(f"my name is \n {name},age is {age},my list is {list1[0]}")
print(f"my name is {name.upper()}")
print(f'result is {(lambda x:x+1)(2)}') #result is 3
