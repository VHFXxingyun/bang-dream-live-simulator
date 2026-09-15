import random
def band_performance():         #随机事件——演出表现随机数
    return round(random.uniform(0.8,1.2),2)
def member_choice(band):            #随机事件——乐队成员选择
    return random.choice(band.members)
def member_performance():       #随机事件——乐队成员表现
    return random.choice(["normal","good","poor"])