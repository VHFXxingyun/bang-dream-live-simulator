import time
from data import bands
from random_events import band_performance,member_choice,member_performance
class Live:
    def __init__(self,band,music):
        self.band = band
        self.music = music
        self.performance = band_performance()        #live发挥随机数
        
    def random_event(self):     #随机事件发生
        event_member= member_choice(self.band)       #随机事件选择乐队成员
        event_performance = member_performance()     #随机事件获取乐队成员表现
        event_member.change_performance(event_performance)
        
        print("乐队情况：" + event_member.name + "当前状态为：" + event_performance)
    

    def score(self,band_score,song_score):  #最终分数计算
        base_score = 100                #基础分数
        event_score = 0                 #随机事件分数计算开始
        for member in self.band.members:
            event_score += member.performance
        event_score /= 5                #随机事件分数计算结束
        final_score = base_score*band_score*song_score*self.performance*self.original_song()*event_score
        if(final_score>1000000):
            final_score = 1000000
        return(final_score)
    def rank(self,score):                   #rank计算
        if(score == 1000000):
            return "ALL PERFECT"
        elif(score>900000):
            return "SSS"
        elif(score>850000):
            return "SS"
        elif(score>800000):
            return "S"
        elif(score>700000):
            return "A"
        elif(score>600000):
            return "B"
        elif(score>500000):
            return "C"
        elif(score>400000):
            return "D"
        elif(score>300000):
            return "F"
    def performance_condition(self):        #乐队发挥水平
        if(self.performance > 1.1):
            return "Fever time！ 演出大成功！！！"
        elif(self.performance > 1.0):
            return "队员状态火热，全场热情四射！"
        elif(self.performance > 0.9):
            return "乐队状态欠佳，未来继续加油吧！"
        elif(self.performance >= 0.8):
            return "演出出现较多差错，尽全力了吗？"
    def live_animation(self):               #演出动画
        print("live进行中")
        for _ in range(10):
            print("■",end="",flush=True)
            time.sleep(0.5)
        print("")
    def original_song(self):                #音乐为所属乐队音乐 获得1.1倍加成
        if(self.band == self.music.affiliation):
            print("获得本家乐队加成！！！")
            return 1.1
        else:
            return 1
    def live(self):                         #live进行
        print("接下来是由" + self.band.name + "带来的音乐：" + self.music.name) #开场介绍
        self.live_animation()                       #演出动画
        self.random_event()                         #随机事件发生
        print(self.performance_condition())         #乐队发挥水平展示
        print("live加成倍率:",self.performance)      #live倍率显示
        final_score = self.score(self.band.power,self.music.score)#计算最终分数
        print("LIVE得分:",round(final_score))          #最终分数显示
        final_rank = self.rank(final_score)            #计算rank
        print("最终评级:",final_rank)                   #rank显示
        for member in self.band.members:
            member.performance_restart()