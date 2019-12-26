### day09

#### 今日内容

- 三元运算
- 函数

#### 内容详细

##### 1.三元运算(三目运算)

```
v=前面 if 条件 else 后面

等于：
if 条件：
	v=前面
else：
	v=后面
```

```
#让用户输入值，如果值为整数，则转换成整数，否则赋值为None
data=input('>>>')
value=int(data) if data.isdecimal() else None
```

##### 2.函数

之前写的都是面向过程。【可读性差/可重用性差】

2.1函数的基本结构

```
#函数的定义
def 函数名()
	#函数内容
	pass
#函数执行
函数名()
```

```
def get_list_first_data():
	v=[11,22,33,44,55]
	print(v[0])
get_list_first_data()
```

2.2参数

​	可以传多个

```
def get_list_first_data(aaa):#形式参数（形参）
	v=[11,22,33,44,55]
	print(v[aaa])
get_list_first_data(1)#实际参数（实参）
```

练习题：

```
v=[11,22,33,44,55]

def s(a):
    print(a)
    sum = 0
    for i in a:
        sum+=int(i)
    return sum
print(s(v))
```

返回值

```
def func(arg):
	#...
	return 9 #返回值9 ，默认返回None

#函数可以返回 任意数据

```

练习

```
#1.让用户输入一段字符串，计算字符串中有多少A字符的个数，有多少个就在文件a.txt中写多少个‘luwei’
def get_char_count(data):
    sum_count=0
    for i in data:
        if i =='A':
            sum_count+=1
    return sum_count

def write_file(data):
    if len(data)==0:
        return False #函数执行过程中，一旦遇到return，则停止函数的执行
    with open('a.txt',mode='w',encoding='utf-8') as f:
        f.write(data)
        return True
content=input('>>')
counter=get_char_count(content)
line='luwei'*counter
status=write_file(line)
if status:
    print('ok')
else:
    print('no')
```

2.4

```
def f1():
	pass
	
def a(b,c):
    return b,c

q,w=a(1,2)

print(q,w)

```



2.5练习题

```
#1.写函数，计算一个列表中有多少个数字。
def num_int(l1):
    n=0
    for i in l1:
        if type(i)==int:
            n+=1
    return n

l=[1,2,13,'a','b','asd']
count=num_int(l)
print(count)
```

```
#2.写函数 计算一个列表中偶数索引位置的数据够成另一个列表返回
def list_data(list_new):
    list1=[]
    for i in list_new[::2]:
        list1.append(i)        
    return list1
    
    
def list_data(list_new):
    list1=[]
    for i in range(0,len(list_new)):
    	if i%2==0:
        	list1.append(i)        
    return list1
   
   
def list_data(list_new):
    list1=list_new[::2]       
    return list1

l=[1,2,13,'a','b','asd']
l1=list_data(l)
print(l1)
```

```
#3.读取文件，将文件内容构造成指定格式的数据，并返回
'''
a.log文件
    alex|123|18
    aric|uniut|19
--------------------
目标结构
a.['alex|123|18','aric|uniut|19']
b.[['alex','123','18'],['eric','uniut','19']]
c.[{'name':'alex','psd':'123','age':'18'}，
	{'name':'eric','psd':'uniut','age':'19']
'''

print('''
***********请输入*********
1.字符
2.列表
3.字典''')
user_choice=input('>>>:')

def str_d():
    l=[]
    with open('a.txt',mode='r',encoding='utf-8') as f:
        for line in f.readlines():
            l.append(line.strip())
        return l

def list_d():
    l=[]
    with open('a.txt',mode='r',encoding='utf-8') as f:
        for line in f.readlines():
            data=line.strip().split('|')
            l.append(data)
        return l



def dict_d():
    l = []
    with open('a.txt',mode='r',encoding='utf-8') as f:
        for line in f.readlines():
            d = {}
            data=line.strip().split('|')
            d['name']=data[0]
            d['psd']=data[1]
            d['age']=data[2]
            l.append(d)
        return l


if user_choice=='1':
    print(str_d())
elif user_choice=='2':
    print(list_d())
elif user_choice=='3':
    print(dict_d())
else:
    print('input errors')
    
    
```

