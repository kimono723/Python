#月饼问题
#公司采购了100个月饼，每个盒子放三个，一共花了多少个盒子，又有多少个没包装的月饼

from re import A


MoonCookie=100
Box=3
BoxNum=MoonCookie//Box
print(f"一共花了{BoxNum}包装盒来包装月饼。")
left=100-3*BoxNum
print(f"\n一共有{left}个月饼没有包装。")

#与或非的使用
a=1>2
b=1<2
print(a and b)
print(a or b)
print(not(a))
