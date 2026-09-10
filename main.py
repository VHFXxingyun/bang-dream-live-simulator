from data import bands,music
from live import Live
print("==========================")
print("BanG Dream! Live Simulator")
print("==========================")
def get_choice (max_num):
    while True:
        try:
            user_input = int(input())
            if (max_num>=user_input>0):
                return user_input
            else:
                print("请输入列表中的数字编号！")
        except ValueError:
            print("非法输入！请输入数字编号！")

        except KeyboardInterrupt:
            print("睦子米呆住了，为什么要说这么坏心眼的话 ;w; (live取消)")
            exit()

if(__name__ == "__main__"):
    print("请选择你的银河战舰：")
    for band in bands:
        print(band.index,band.name)

    print("前方登场的是————————")
    choose_band= get_choice(len(bands))     #获取乐队
    bands[choose_band - 1].show_members()   
    bands[choose_band - 1].introduce()      #开场白方式

    print("请选择你的live歌曲:")                #展示乐队列表
    for song in music:
        print(song.index,song.name)
    choose_music = get_choice(len(music))               #获取歌曲

    live = Live(bands[choose_band - 1],music[choose_music - 1])          #导入live数据
    live.live()             #进行live