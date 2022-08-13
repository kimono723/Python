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
