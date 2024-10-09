import keyboard
import time
import random

game_start = 0
mapstart = 0
snakekakudo = 'd'
gameover = 0


while game_start == 0:
    mapsize = input('マップの大きさを8～20で決めてください')
    mapsize = int(mapsize)
    if 8 <= mapsize <= 20:
        game_start = 1
        #マップが5～20の場合進める
    else:
        print('5～20で選んでください')
        #それ以外ならwhileを使用して戻す
#マップの大きさを決めるプログラム
while game_start == 1:
    skin = input('キャラクターとなる文字を全角で入力してください\n')
    if len(skin) == 1:
        game_start = 2
        #キャラクターが一文字なら進める
    else:
        print('1文字にしてください')
        #1文字出なかった場合繰り返す
apple = '🍎'
apple_zahyou = ((mapsize + 1)* 3 + 5)
score = 0
zahyou = ((mapsize + 1)* 3 + 1)
mapx = list(range(mapsize))
mapy = list(range(mapsize))

#マップ（文字列）をリスト化したあとキャラを反映させ文字列に戻す関数
map2 = ["〇" * len(mapx) + "\n"]
def mapkansuu(map):
    for map in map2:
        map = [map * len(mapy)]
        for map in map:
            map = list(map)
            #マップをリスト化       
            maplist = map[zahyou]
            #キャラクターの座標の文字を抽出
            map[apple_zahyou] = apple
            map[zahyou] = skin        
            map = "".join(map)
            print(map)
            #マップを文字列化

a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]

#進むプログラムを繰り返す
#マップの端に着いたら死ぬプログラム
while gameover == 0:
    zahyoudake  = (zahyou + 1) / (mapsize + 1)
    if zahyoudake ==  float(zahyoudake // 1):
        zahyoudake = int(zahyoudake)
        if zahyoudake == 1 or 2 or 3:
            gameover = 1
            break
    if not keyboard.is_modifier('w' and 'a' and 's' and 'd'):
        mapkansuu(map)

#キーが押されたら進むプログラム
        start_time = time.time()
        while True:
            elpased_time = time.time() - start_time
            if keyboard.is_pressed('w'):
                snakekakudo = 'w'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('d'):                    
                snakekakudo = 'd'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('a'):
                snakekakudo = 'a'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('s'):
                snakekakudo = 's'
                time.sleep(0.1)
                break
            elif elpased_time >= 0.1:
                snakekakudo = snakekakudo
                break

        #ヘビが常に進むプログラム↓
    while True:
        if gameover == 1:
            break
        elif snakekakudo == 'w':
            zahyou -= (mapsize+1)
            time.sleep(0.1)
            break
        elif snakekakudo == 's':
            zahyou += (mapsize+1)
            time.sleep(0.1)
            break
        elif snakekakudo == 'a':
            zahyou -= 1
            time.sleep(0.1)
            break
        elif snakekakudo == 'd':
            zahyou += 1
            time.sleep(0.1)
            break

#リンゴをランダムに配置するプログラム
    while True:
        if apple_zahyou == zahyou:
            apple_map_reset = 0
            score += 1
            while apple_map_reset == 0:
                apple_zahyou = random.randint(0, mapsize ** 2)
                if not (apple_zahyou / (mapsize + 1)) in a:
                    apple_map_reset = 1
                    break
        else:
            break

print('Gmae Over!')
print('score is',score)
game_start = 1