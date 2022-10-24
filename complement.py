#import----------------------------------------
import csv
from re import A
import pandas as pd
import numpy as np
import JSONtoCSV
import os
from scipy.signal import argrelmin, argrelmax
#----------------------------------------------

#parameters------------------------------------

# サンプリング周波数[Hz]
Fs = 30
# 距離(m)
distance = 5
# 快適速度と転倒危険性[m/s]
true_speed = [0.6, 1.22]
# 健康変動性
true_variability = [2,3]
# 健康対称性と脳卒中患者
true_symmetry = [1.02, 1.23]

#func------------------------------------------

# 速度
def speed(df,comfortable_speed,distance,Fs):

    # 速度=距離[m]/時間[s]
    return distance/(len(df)/Fs)

# 変動性
def variability(df):

    # 移動平均
    df['avg'] = df['Y-axis_24'].rolling(15).sum()

    # 極小値を見つける -> peaksには極小値のindexが格納される
    peaks = argrelmin(df['avg'].values)

    # 極小値間の時間を計算
    diffs = np.array([])
    pre = 0

    for f in peaks[0]:
        if pre == 0:
            pre = f
            continue

        diffs = np.append(diffs, f-pre)
        pre = f

    return np.std(diffs)/np.mean(diffs)*100

# 変動性
def symmetry(df,Fs):

    # 移動平均
    df['avg_left_toe'] = df['Y-axis_20'].rolling(15).sum()
    df['avg_left_heel'] = df['Y-axis_21'].rolling(15).sum()
    df['avg_right_toe'] = df['Y-axis_23'].rolling(15).sum()
    df['avg_right_heel'] = df['Y-axis_24'].rolling(15).sum()

    list_left_heel = np.asarray(argrelmax(df['avg_left_heel'].values))
    list_right_heel = np.asarray(argrelmax(df['avg_right_heel'].values))
    list_left_toe = np.asarray(argrelmax(df['avg_left_toe'].values))
    list_right_toe = np.asarray(argrelmax(df['avg_right_toe'].values))

    left_heelSize = list_left_heel.shape[1]
    right_heelSize = list_right_heel.shape[1]
    left_toeSize = list_left_toe.shape[1]
    right_toeSize = list_right_toe.shape[1]

    min_left_size = min(left_heelSize-1,left_toeSize)
    min_right_size = min(right_heelSize-1,right_toeSize)

    left_nomadic_time = 0
    right_nomadic_time = 0
    
    for m in range(min_left_size):
        left_nomadic_time += list_left_heel[0][m+1] - list_left_toe[0][m]

    # 左遊脚時間
    left_nomadic_time = left_nomadic_time/(min_left_size*Fs)

    for n in range(min_right_size):
        right_nomadic_time += list_right_heel[0][n+1] - list_right_toe[0][n]

    # 右遊脚時間
    right_nomadic_time = right_nomadic_time/(min_right_size*Fs)

    # 対称性
    symmetry_value = left_nomadic_time/right_nomadic_time if left_nomadic_time > right_nomadic_time else right_nomadic_time/left_nomadic_time

    return symmetry_value

def score(true_speed,true_variability,true_symmetry,speed,variability,symmetry,filepath):

    # 速度
    # 健康
    if speed > true_speed[1]:
        speed_socre = 100
    # 転倒リスクあり
    elif speed < true_speed[0]:
        speed_score = 0
    else:
        speed_score = round((speed-true_speed[0])*100/(true_speed[1]-true_speed[0]))

    # 変動性
    # 健康
    if variability >= true_variability[0] and variability <= true_variability[1]:
        var_score = 100
    # 不安定
    elif variability > true_variability[1]:
        var_score = 100 - (round(variability,2) - true_variability[1])*100
    # 柔軟性が乏しい
    else:
        var_score = round(100 - (true_variability[0] - round(variability,2))*100)

    # 対称性
    # 健康
    if symmetry < true_symmetry[0]:
        sym_score = 100
    # 脳卒中
    elif symmetry > true_symmetry[1]:
        sym_score = 0
    else:
        sym_score = 100 + round((symmetry-true_symmetry[0])*(-100)/(true_symmetry[1]-true_symmetry[0]))

    # 総合点，総合ランク
    all_score = speed_score+var_score+sym_score

    if all_score > 240:
        walking_rank = "S"
    elif all_score <= 240 and all_score > 220:
        walking_rank = "A"
    elif all_score <= 220 and all_score > 200:
        walking_rank = "B"
    else:
        walking_rank = "C" 

    # 結果の出力
    print("結果")
    print("速度：{:.2f}[m/s]".format(speed))
    print("変動性：{:.2f}[%]".format(variability))
    print("対称性：{:.2f}[%]".format(symmetry))
    print(" ")
    print("速度のスコア：",speed_score,"点")
    print("変動性のスコア：",var_score,"点")
    print("対称性のスコア：",sym_score,"点")
    print(" ")
    print("総合点：",all_score,"点")
    print("総合ランク",walking_rank)

    # 書き込み
    f = open(os.path.join("./",input,"result.txt"), 'w')
    f.write(str(speed_score)+'\n')
    f.write(str(var_score)+'\n')
    f.write(str(sym_score)+'\n')
    f.write(str(all_score)+'\n')
    f.write(str(walking_rank)+'\n')
    f.close()



#main------------------------------------------
if __name__ == "__main__":

    # preparation
    print("data.csvの保存先（フォルダ）を入力してください")
    input = input()

    # filename
    filepath = os.path.join("./",input)
    filename = os.path.join("./",input,"data.csv")

    if os.path.exists(filename) == False:
        JSONtoCSV.jtc(input)

    # Pandas
    indicator = ["X-axis","Y-axis","Credibility"]
    col_names = [j + '_' + str(i) for i in range(25) for j in indicator]
    col_names.insert(0,"keypoints")
    df = pd.read_csv(filename, encoding='cp932',names=col_names)
    df = df[~(df["X-axis_0"]==' {"version":1.3')]
    df.iloc[:,1:3] = df.iloc[:,1:3].astype('float')

    # interpolate
    df = df.replace(0, np.nan)
    df = df.interpolate()
    df.to_csv(filename[:-4]+"_complemented.csv",index=False)

    variability = variability(df)
    speed = speed(df,true_speed,distance,Fs)
    symmetry = symmetry(df,Fs)
    score(true_speed,true_variability,true_symmetry,speed,variability,symmetry,filepath)