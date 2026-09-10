import time
import random
class Live:
    def __init__(self,band,music):
        self.band = band
        self.music = music
        self.rate = round(random.uniform(0.8,1.2),2)
    def score(self,band_score,song_score):  #最终分数计算
        base_score = 100
        final_score = band_score*song_score*base_score*self.performance_rate()*self.original_song()
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
    def performance_rate(self):             #乐队发挥分数
        return self.rate
    def performance_condition(self):        #乐队发挥水平
        if(self.rate > 1.1):
            return "Fever time！ 演出大成功！！！"
        elif(self.rate > 1.0):
            return "队员状态火热，全场热情四射！"
        elif(self.rate > 0.9):
            return "乐队状态欠佳，未来继续加油吧！"
        elif(self.rate >= 0.8):
            return "出现较多差错，尽全力了吗？"
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
        print("接下来是由" + self.band.name + "带来的音乐：" + self.music.name)
        self.live_animation()
        print(self.performance_condition())         #计算加成
        print("live加成倍率:",self.performance_rate())
        final_score = self.score(self.band.power,self.music.score)#计算最终分数
        print("LIVE得分:",round(final_score))
        final_rank = self.rank(final_score)
        print("最终评级:",final_rank)