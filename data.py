from models import Band,Music,Character

bands = [
    Band("Ave Mujica",[Character("丰川祥子","piano"),Character("三角初华","vocal"),Character("若叶睦","guitar"),Character("八幡海铃","bass"),Character("祐天寺若麦","drum")],95,"「欢迎来到 Ave Mujica的世界」",1),
    
    Band("MyGO!!!!!",[Character("千早爱音","guitar"),Character("高松灯","vocal"),Character("要乐奈","guitar"),Character("长崎素世","bass"),Character("椎名立希","drum")],85,"你愿意和我组一辈子乐队吗？",2),
    
    Band("Poppin'Party",[Character("市谷有咲","piano"),Character("户山香澄","vocal"),Character("花园多惠","guitar"),Character("牛込里美","bass"),Character("山吹沙绫","drum")],90,"大家一起闪闪发光吧！",3),
    
    Band("Roselia",[Character("白金燐子","piano"),Character("凑友希那","vocal"),Character("冰川纱夜","guitar"),Character("今井莉莎","bass"),Character("宇田川亚子","drum")],93,"我们是「Roselia」",4),
    
    Band("RAISE A SUILEN",[Character("PAREO","piano"),Character("LAYER","vocal"),Character("LOCK","guitar"),Character("CHU²","DJ"),Character("MASKING","drum")],93,"「We are RAISE A SUILEN!」",5),
]

music = [
    Music("Imprisoned XII",bands[0],82,1),
    Music("KiLLKiSS",bands[0],94,2),
    Music("天球のMúsica",bands[0],90,3),
    Music("迷星叫",bands[1],88,4),
    Music("Ringing Bloom",bands[3],90,5),
    Music("Returns",bands[2],87,6),
    Music("LOUDER",bands[3],92,7),
    Music("春日影(MyGO!!!!! ver.)",bands[1],86,8),
    Music("Ave Mujica",bands[0],92,9),
]