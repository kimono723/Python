from ctypes.wintypes import HPALETTE
from operator import truediv
import random
from re import A
from sys import dont_write_bytecode
from time import daylight
abc=random.random()
print(abc)

MyMoney=218+175
print(MyMoney)

result=77+66
print(result)

number1=77
number2=66
result=number1-number2
print(result)

result=16%3
print(result)

Date="2018年10月3日"
Day="星期三"
print(Date+Day)

#格式化输出print(f"内容{变量}")
name='Downey'
birthday=19650404
print(f"his name is {name}")
print(f"his birthday is {birthday}")

a=True
b=False
Result1=a or b
print(Result1)

#if判断
MyWeight=95
canRide=True
if MyWeight>90:
    print("超过体重限制！")
    canRide=False
print(canRide)

MyWeight=70.5
YourWeight=81.3
if MyWeight<YourWeight:
    print("you are heavier than me.")

hp=100
damage=210
if hp -damage<=0:
    print("角色死亡")
    print("游戏结束")

#五行代码
MyHeight,YourHeight,HerHeight=172,175,181
Result1=(MyHeight>YourHeight) and (YourHeight>HerHeight)
print(Result1)

#题目1：
#   大学开学前，jack想换一个手机，但jack只有6000元，那么在新一代的手机里，他能换哪一部手机呢
#以下数据来源于2019.8.21京东实时数据
#iPhone XR=5099
#iphone XS=7299
#xiaomi I9=3599
#huawei p30pro=5488

JackMoeny=6000
iphonexr=5099
iphonexs=7200
xiaomii9=3699
huaweip30pro=5488

List=[]

if JackMoeny>=iphonexr:
    print(f"可以购买{iphonexr}的苹果xr")
    List.append(JackMoeny-iphonexr)
    print(f"剩余{JackMoeny-iphonexr}元")
if JackMoeny>=iphonexs:
    print(f"可以购买{iphonexs}的苹果xs")
    List.append(JackMoeny-iphonexs)
    print(f"剩余{JackMoeny-iphonexs}元")
if JackMoeny>=xiaomii9:
    print(f"可以购买{xiaomii9}的小米i9")
    List.append(JackMoeny-xiaomii9)
    print(f"剩余{JackMoeny-xiaomii9}元")
if JackMoeny>=huaweip30pro:
    print(f"可以购买{huaweip30pro}的华为p30pro")
    List.append(JackMoeny-huaweip30pro)
    print(f"剩余{JackMoeny-huaweip30pro}元")

print(List)
Max=max(List)
print(f"其中最便宜的是小米i9，一共便宜了{Max}")

#鸡腿与运动问题,如果一天超过五个就要运动。
drumstick=3
if drumstick>5:
    print(f"yes,需要跑步,今天吃了{drumstick}个鸡腿")
else:
    print(f"no，不需要，今天吃了{drumstick}个鸡腿")

MyHeight,YourHeight=171,181
if MyHeight>YourHeight:
    print("还是我更高！")
else:
    print("还是你更高!")

#7 line code
CityPopulation=100000
if CityPopulation<=50000:
    print("small city!")
elif (CityPopulation<=400000) and (CityPopulation>50000):       #elif 50000<citypopulation<=400000
    print("middle city!")
else:
    print("big city")
    print(MyMoney)

#做题做题还是做题
FreeKg=20
IfOverKgNeedPay=20
NiMotsu=8.5+6+8
if NiMotsu>FreeKg:
    Over=NiMotsu-FreeKg
    print(f"需要支付{Over*IfOverKgNeedPay}元")
else:
    print("不需要补交运费")

#题目2
a=17*87+343-8*134
if a>0:
    print("正数")
elif a==0:
    print("0")
else:
    print("负数")

List=["kai","kimono","武神铠武","公孙天宜",]
print(List)
print(List[-1])
List.append("suhua")
print(List)

#题目
SpecialDate=[199303035,20100505,20140214]
SpecialDate[0]=19930704
print(SpecialDate)

word="abcdefg"
print(word[0])
print(word[2])

DpecialDate=[19930305,20100505,20140214]
print(DpecialDate)
DpecialDate.append(19930704)
print(DpecialDate)

SpecialDate=[19930305,20100505,20140214]
print(SpecialDate)
SpecialDate.insert(1,19930704)
print(SpecialDate)

SpecialDate=[19930305,20100505,20100505,20140214]
print(SpecialDate)
#del(SpecialDate[-1])
lastDate=SpecialDate.pop()
print(SpecialDate)
print(lastDate)

dayList=["星期日","星期二","October","星期三","星期五"]
del(dayList[2])
print(dayList)
dayList.insert(1,"星期一")
dayList.insert(4,"星期四")
#dayList.insert(6,"星期六")
dayList.append("星期六")
print(dayList)

list1=[1,2,3,4]
list1.pop(0)
list1.insert(0,4)
list1.pop(1)
list1.insert(1,3)
list1.pop(2)
list1.insert(2,2)
list1.pop(3)
list1.insert(3,1)
print(list1)

AgeList=[18,19,21,22,24]
for oneAge in AgeList:
    print(oneAge)

a=range(30)
print(list(a))

sum=0
for i in range(1001):
    sum=sum+i
print(sum)

NewList=[]
for i in range(101):
    if i%2==0:
        NewList.append(i)
print(NewList)

jiage=0
price=[3,15,11,9,12,3,9,15,18,14]
for i in price:
    jiage=jiage+i
print(jiage)

NumList=[83,80,18,4,88,21,96,20,40,59]
MaxNumber=NumList[0]
for i in NumList:
    if i>MaxNumber:
        MaxNumber=i
print(MaxNumber)

bool=1
i=0
#while bool==1:
#    i=i+1
#    print(i)

Nub=5
while Nub<=10:
    print(Nub)
    Nub=Nub+1
    
a=0
for i in range(101):
    a=a+i
print(a)

i=1
while i<=10:
    print("*"*i)
    i=i+1
