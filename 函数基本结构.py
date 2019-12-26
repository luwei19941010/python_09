
#-*-coding:utf-8-*-
# Author:Lu Wei

"""
########参数#######
def get_list_first_data(aaa):#形式参数（形参）
	v=[11,22,33,44,55]
	print(v[aaa])
get_list_first_data(1)#实际参数（实参）

######
v=[11,22,33,44,55]

def s(a):
    print(a)
    b = 0
    for i in a:
        b+=i
    return b

print(s(v))





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

def num_int(l1):
    n=0
    for i in l1:
        if type(i)==int:
            n+=1
    return n

l=[1,2,13,'a','b','asd']
count=num_int(l)
print(count)


def list_data(list_new):
    list1=[]
    for i in list_new[2::2]:
        list1.append(i)
    return list1

l=[1,2,13,'a','b','asd']
l1=list_data(l)
print(l1)



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

"""

