#-*-coding:utf-8-*-
# Author:Lu Wei
#让用户输入值，如果值为整数，则转换成整数，否则赋值为None
data=input('>>>')
value=int(data) if data.isdecimal() else None
d={}
print(type(d))

a=['alex','123','18']
b=['eric','uniut','19']
a.append(b)
print(a)