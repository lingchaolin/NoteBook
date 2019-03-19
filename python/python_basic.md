Python把在程序中用到的任何东西都称为 对象 。

变量

* * *

#### 打印字符串
```python
print("字符串")

var="字符串变量"   # 弱类型，不需要定义
print(var)
```
变量的命名和使用
```
    变量名只能包含字母、数字和下划线，且不能以数字开头。
    不要将Python关键字和函数名用作变量名
    见名知意--变量名应既简短又具有描述性
    慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
```
字符串：
```python
单双引号括起来的--单双引号可以相互包含，字符串中可以包含引号
title()方法：--单词首字母大写
upper():全部大写
lower():全部小写

拼接字符串 '+'
print("abc"+"123")
print("abc"+str(123))  
print("abc",123)--不同类型的拼接

删除空白----类似trim
user="  张  三  "
print(user)
print(user.lstrip()) #lstrip:去除左端空白
print(user.rstrip()) #rstrip:去除右端空白
print(user.strip())  #strip:去除两端空白
```
数字
```python
数字：
>>> 1+2  #'+'
3
>>> 3-1 #'-'
2
>>> 2*3 #'*'
6
>>> 6/2 #'/'
3.0
>>> 2**3 #'乘方'
8
>>> (2+3)*6 #运算优先级、小括号
30

类型转换：str()--转换成字符串
age=23
mes="happy "+age+" birthday"
print(mes)
#报错：age为int类型，需要将其转换为字符串类型
age=23
mes="happy "+str(age)+" birthday"
print(mes)
注释： #
```
列表：
```python
列表初始化
  arrays=["index0","index1","index2"]
  print(arrays)      #打印结果：['index0', 'index1', 'index2']
列表取值
  print(arrays[1]) #根据序号取数据，索引从0 开始
修改列表
  arrays[1]=23       #可以存放不同的类型 ['index0', 23, 'index2']
  arrays[-1]：取最后一个元素
  arrays[-3]：取倒数第三个元素
  arrays=["tom","jerry","puffy"]

添加元素
  #append()添加
  arrays.append("happy") #在列表末尾添加
插入元素
  #insert()插入
  arrays.insert(1,"newData") #在指定索引处插入数据
删除元素
  #del()删除
  del arrays[1] #按索引删除
  #pop()弹出
  arrays.pop() #删除末尾的元素
  arrays.pop(0) #按照索引删除

/*如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；如果你要在删除元素后还能
继续使用它，就使用方法pop()*/
#sort()排序
arrays=["tom","jerry","puffy","happy"]
arrays.sort() #永久性修改元素的排列顺序
print(arrays)
arrays.sort(reverse=True) #与字母顺序相反的顺序显示
print(arrays)
#sorted()--临时排序，不影响列表原本的顺序
print(sorted(arrays))
print(sorted(arrays,reverse=True))
#reverse() 反序
arrays.reverse()
print(arrays)
#len()确定列表长度
print(len(arrays))
```



* * *

第四章：操作列表

arrays=["tom","jerry","puffy","happy"]

#for循环

for per in arrays:#遍历数组中的元素

      print(per)

#range():指定区间的数字

for val in range(1,5):#

      print(val)

#list() 将参数转换为列表

numbers=list(range(1,6))

print(numbers)

numbers=list(range(2,12,3))#指定步长

print(numbers)

#对数字列表执行简单的统计计算

digits=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min(digits)#最小值

max(digits)#最大值

sum(digits)#取和

#for循环定义数组

arr=[val**2 for val in range(1,11)]

print(arr)

#使用列表的一部分：切片

digits=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(digits[0:5])

print(digits[5:])#索引为5的开始，直到最后一位

print(digits[:5])#索引从0开始，到最后一位

#复制列表--创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:] ）

newdata=digits[:]#newdata与digits不是同一个列表

print(newdata)

new=digits#二者指向同一个列表

* * *

元组：不可变的列表

arr=("data",12)#元组

print(arr)

for val in arr:

      print(val)

print(list(arr))

* * *

第五章 if语句

#if判断

# '=='是否相等，不考虑大小写

num=12

if num==12:

      print("yes")

else:

      print("no")

#'!='检查是否不相等

# '<' '<=' '>' '>='

#使用'and' 'or'检查多个条件

print(1==1 and 2==2)

#'in' 列表是否包含特定值

arr=[1,2,3,4,5]

print(3 in arr)

#'not in' 列表是否不包含特定值

#if-elif-else

age=16

if age<12:

      print("儿童")

elif age<18:

      print("青年")

else:

      print("成年")

#if 数组arr:若列表为空，则boolean值为false,否则为true

brr=[]

if brr:

      print("arr不为空")

else:

      print("arr为空")

* * *

第六章 字典：

键值对

#定义字典

alien={'color':'red','points':5}

print(alien['color'])--取值

print(alien)

#添加元素/修改

alien['name']='张三' --赋值

print(alien)

#删除

del alien['name']

print(alien)

#创建空字典

alien_0={}

迭代器，迭代遍历

#遍历键值对

for k,v in alien.items():

      print(k,v)

#遍历字典中的键

for k in alien.keys():

      print(k)

#按顺序遍历字典中的所有键

for k in sorted(alien.keys()):

      print(k)

#遍历字典中的所有值

for v in alien.values():

      print(v)

#使用集合set：剔除重复项

for v in set(alien.values()):

      print(v)

#在字典中存储列表

alien={

      'name':'张三',

      'subjects':['语文','数学','英语']

}

print(alien)

#在字典中存储字典

users = {

        'aeinstein': {

              'first': 'albert',

              'last': 'einstein',

              }

       }

* * *

input（）输入函数和while循环

#input()输入函数：

#int() 将数字的字符串表示转换为数值表示

#求模运算 %

#wwhile循环

num=1

while num<5:

      print(num)

      num=num+1

#删除包含特定值的所有列表元素

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:

pets.remove('cat')

print(pets)

alien={}

flag=Truewhile flag:

name=input("\n请输入名字！")

age=input("\n请输入年龄！")

alien["name"]=name

alien["age"]=age

flag=Falseprint(alien)

* * *

函数

#定义函数

def test():

               print("新建函数")

#调用

test()

#传参

def two(num):

               print("结果："+str(num**2))

two(3)

def three(id,name):

               print("id:"+id+",name:"+name)

three("123","张三")

three(id="123",name="张三")

#参数设置默认值

def four(name,type='dog'):

               print("姓名："+name+",品种："+type)

four("大黄")#有默认值，可以不输入参数

#返回值

def retname():

               return "张三"

name=retname()

print(name)

#返回字典

#函数结合循环

#传递列表

#在函数中修改列表

#禁止函数修改列表--将列表的副本传进来

def function_name(lists):

               print("列表的副本")

list=["1",2,"3"]

function_name(list[:])

#传递任意数量的实参

def multi(*tops):

               print(tops)

multi("张三","李四","王五")

#结合使用位置实参和任意数量实参

#任意数量实参放到最后

def make_pizza(size, *toppings):

#使用任意数量的关键字实参

* * *

#将函数存储在模块中,import 语句允许在当前运行的程序文件中使用模块中的代码。

test.py

    def imptest():

               print("这个文件名是：test.py")

second.py

    import test #导入

    test.imptest() #调用

#将函数存储在模块中,import 语句允许在当前运行的程序文件中使用模块中的代码。

def imptest():

               print("这个文件名是：test.py")

#import test #导入

#test.imptest() #调用

#导入特定的函数

from module_name import function_name

# 使用as 给函数指定别名

from pizza import make_pizza as mp

mp(16, 'pepperoni')

#导入模块中的所有函数

from pizza import *




 #定义类

class Dog():

               def __init__(self,name,age):#构造方法前后的下划线为两个

                              #self 为前缀的变量都可供类中的所有方法使用，

                              #我们还可以通过类的任何实例来访问这些变量

                              self.name=name

                              self.age=age

                              print("构造方法")

               def bite(self):

                              print("汪汪汪:"+self.name)

               def eat(self):

                              print("啃骨头："+self.name)

my_dog = Dog("大黄","6")

my_dog.bite()

my_dog.eat()

#修改属性--也可以通过方法修改属性值

my_dog.name="小黑"

my_dog.eat()

#继承--子类

class LittleDog(Dog):

               def __init__(self,name,age,field):

                              #调用父类的 init 方法--父类，超类

                              super().__init__(name,age)

                              self.field=field#子类的新参数

               #子类的新方法

               def newMethod(self):

                              print("子类的新方法："+self.field)

               #重写

               def eat(self):

                              print("子类重写方法：啃骨头："+self.name)

ldog=LittleDog('jerry',2,"参数A")

ldog.eat()

ldog.newMethod()

#将实例用作属性

#

#从一个模块中导入多个类

from car import Car, ElectricCar

#random模块中的randint函数？

from random import randint

x=randint(1,7)

print(x)

* * *

第十章 文件和异常

#读取文件   Python将在当前执行的文件（即.py程序文件）所在的目录中查找文件。

with open('second.txt','rb') as file_object:

    contents = file_object.read()

    print(contents)

print("---分界线---")

with open('second.txt','r',encoding='UTF-8') as file_object:

    contents = file_object.read()

    print(contents)

#可以指定路径，读取路径下的文件

#逐行

with open('second.txt','r',encoding='UTF-8') as file_object:#一行一行检查

    for line in file_object:

           print(line)

#创建一个包含文件各行内容的列表

with open('second.txt','r',encoding='UTF-8') as file_object:

               lines=file_object.readlines()

print(lines)

#写入文件

with open('second.txt','w') as file_object:

    contents = file_object.write("write test 写入测试")

with open('second.txt','w',encoding='UTF8') as file_object:

    contents = file_object.write("write test 写入测试")

#PS:

open('……','w') w-清空文件/创建文件，然后写入

open('……','a') a-附件模式

open('……','r') r-读取文件

open('……','r+') r+ 读取和写入

#若省略了模式实参,默认是只读模式

# 异常

try:

               print(5/2)

except ZeroDivisionError:

               print("除数不能为0，报错")

else:

               print("正常运行")

# FileNotFoundError

#

#统计字数

with open("贩罪.txt") as file:

               contents=file.read()

               words=contents.split('')

               num=len(words)

               print("字数："+str(num))

               print(words)

#json.dump() 存储数据

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:

    json.dump(numbers, f_obj)

#json.load() 读取数据

with open(filename, 'r') as f_obj:

               number=json.load(f_obj)

               print(number)

# 重构？？

* * *

第十一章：测试代码

* * *

在Python语言中，json数据与dict字典以及对象之间的转化，是必不可少的操作。

在Python中自带json库。通过import json导入。

在json模块有2个方法，

*   loads()：将json数据转化成dict数据

*   dumps()：将dict数据转化成json数据

*   load()：读取json文件数据，转成dict数据

*   dump()：将dict数据转化成json数据后写入json文件

* * *

脚本初涉

import re #

import chardet #编码

import json #json数据的读写

#更新字典

class Update_dict():

    def __init__(self,source_file="",dict_file=""):

        self.source_file=source_file

        self.dict_file=dict_file

        try:

            charset=self.get_encode(self.source_file)

            self.source_charset=charset if(charset!="GB2312") else "GBK"

            self.dict_charset=self.get_encode(self.dict_file)

        except FileNotFoundError:

            print("找不到文件，请检查路径是否正确！")

    #返回编码格式

    def get_encode(self,file_path):

        with open(file_path,"rb") as txtfile:

            data=txtfile.read().lstrip()[0:100]#去除左边空格，取前99？个字符

            txtfile.close()

            chardict=chardet.detect(data)#识别字符编码类型

            return chardict['encoding']

    def new_dict(self):

        dictmap={}

        dictmap_json=""

        #读取字典--从文件中读取数据，转换成字典文件

        with open(self.dict_file,"r+",encoding=self.dict_charset) as dictfile:

            json_dict=dictfile.read()

            dictfile.close()

            if json_dict!="":

                dictmap=eval(json_dict)

        #,errors='ignore'

        with open(self.source_file,"r",encoding=self.source_charset) as txtfile:

            content=txtfile.read()

            txtfile.close()

            rule="[\u4000-\u9fa5]{0,1}[a-zA-Z*]{1,10}[\u4000-\u9fa5]{0,1}|[\u4000-\u9fa5]{1,5}[*]{1,20}[\u4000-\u9fa5]{1,5}"

            reg=re.compile(rule)

            listing=re.findall(reg,content)#存放在list列表中

            # print(listing)

            for examp in listing:

                if examp in dictmap.keys():

                    continue

                dictmap[examp]=examp

            sorted_dictmap=sorted(dictmap.items(),key = lambda item:item[1],reverse=True)

            dictmap={}

            for per in sorted_dictmap:

                dictmap[list(per)[0]]=list(per)[1]

            ##加上ensure_ascii=False后data返回的就是中文而不是unicode

            dictmap_json=json.dumps(dictmap,ensure_ascii=False)

        # print(dictmap)

        #写入字典

        with open(self.dict_file,"w+",encoding=self.dict_charset) as dictfile:

            dictfile.write(dictmap_json)

            dictfile.close()

    #整理字典：--

    def clear_dict(self):

        with open(self.dict_file,"r+",encoding="UTF-8") as dictfile:

            json_dict=dictfile.read()

            dictfile.close()

            if json_dict!="":

                self.dictmap=eval(json_dict)

        for examp in list(self.dictmap):

            if self.dictmap[examp]==examp:

                del(self.dictmap[examp])

        sorted_dictmap=sorted(self.dictmap.items(),key = lambda item:item[1],reverse=True) 

        dictmap={}

        for per in sorted_dictmap:

            dictmap[list(per)[0]]=list(per)[1]

        dictmap_json=json.dumps(dictmap,ensure_ascii=False)

        # self.dictmap_json=json.dumps(self.dictmap,ensure_ascii=False)

        with open(self.dict_file,"w+",encoding="UTF-8") as dictfile:

            dictfile.write(dictmap_json)

            dictfile.close()

#根据字典文件，将目标文本中字典匹配的内容替换

def fixTxt(self):

        content=""

        content=""

        dictmap={}

        try:

            with open(self.source_file,"r+",encoding=self.source_charset) as txtfile:

                content=txtfile.read()

                txtfile.close()

        except UnicodeDecodeError:

            with open(self.source_file,"r+",encoding="GB18030") as txtfile:

                content=txtfile.read()

                txtfile.close()

        with open(self.dict_file,"r+",encoding="UTF-8") as dictfile:

            dictmap=eval(dictfile.read())

            dictfile.close()

        # print(type(dict(dictmap)))

        for examp in dictmap:

            if dictmap[examp]!=examp:

                #处理正则表达式

                key=""

                for each in examp:

                    c_no=ord(each)

                    if  c_no in range(97,123):

                        key=key+"["+each+chr(c_no-32)+"]"

                    elif c_no in range(65,91):

                        key=key+"["+each+chr(c_no+32)+"]"

                    else:

                        key=key+chr(c_no)

                content=re.sub(re.compile(key),dictmap[examp],content)

        with open(self.source_file,"w+",encoding=self.source_charset) as txtfile:

            txtfile.write(content)

            txtfile.close()

   #移除字典中包含的字符串

def remove_advert(source_file="",dict_advert=""):

    updt=Update_dict(source_file,dict_advert)

    try:

        source_charset="GB18030"

        dict_charset=updt.get_encode(dict_advert)

    except FileNotFoundError:

        print("找不到文件，请检查路径是否正确！")

    context=""

    dict_adv={}

    with open(source_file,"r+",encoding=source_charset) as txtfile:

        context=txtfile.read()

        txtfile.close()

    with open(dict_advert,"r+",encoding=dict_charset) as dictfile:

        dict_adv=eval(dictfile.read())

        dictfile.close()

    #print(type(dict_adv))

    for per in dict_adv.keys():

        context=re.sub(re.compile(per),"",context)

    with open(source_file,"w+",encoding=source_charset) as txtfile:

        txtfile.write(context)

        txtfile.close()

* * *

#去除广告

#修正文本--去除拼音

#章节整理
