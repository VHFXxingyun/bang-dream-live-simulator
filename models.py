class Band:
    def __init__(self,name,members,power,opening,index):       #名称 成员 能力 开场白 序列号
        self.name = name
        self.members = members
        self.power = power
        self.opening = opening
        self.index = index
    def introduce(self):                #开场白方法
        print(self.name,self.opening,sep="\n")              #sep 多个参数之间分隔方式
    def show_members(self):             #展示成员方法
        for member in self.members:
            print(member.name,member.role)

class Music:
    def __init__(self,name,affiliation,score,index):        #名称 所属乐队 分数 序列号
        self.name = name
        self.affiliation = affiliation
        self.score = score
        self.index = index

class Character:
    def __init__(self,name,role,performance):              #名称  职责  状态
        self.name = name
        self.role = role
        self.performance = performance
    def change_performance(self,change):
        if(change == "normal"):
            self.performance = 1.0
            return self.performance
        elif(change == "good"):
            self.performance = 1.1
            return self.performance
        elif(change == "poor"):
            self.performance = 0.9
            return self.performance
    def performance_restart(self):
        self.performance = 1.0