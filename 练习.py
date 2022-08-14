from ctypes.wintypes import HPALETTE
import random
from re import A
from sys import dont_write_bytecode
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
