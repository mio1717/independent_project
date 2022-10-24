import tkinter as tk
from PIL import Image, ImageTk
import os
import time


class Application(tk.Frame):
	
	def __init__(self,master = None):
		super().__init__(master)
		self.pack()
		
		#ウィンドウを大きさ・タイトル
		master.geometry("1440x900") #横x縦
		master.title("診断結果：")

		
		# キャンバス作成
		speed = tk.Canvas(master, height=200, width=400) #縦x横 #速度の画像を表示するキャンバス
		variability = tk.Canvas(master, height=200, width=400) #変動性の画像を表示するキャンバス
		symmetry = tk.Canvas(master, height=200, width=400) #対称性の画像を表示するキャンバス

		speed_point = tk.Canvas(master, height=200, width=400) #速度の点数を表示するキャンバス
		variability_point = tk.Canvas(master, height=200, width=400) #変動性の点数を表示するキャンバス
		symmetry_point = tk.Canvas(master, height=200, width=400) #対称性の点数を表示するキャンバス

		score = tk.Canvas(master, height=300, width=400) #総合点を表示するキャンバス
		evaluation = tk.Canvas(master, height=300, width=400) #総合評価を表示するキャンバス
		index = tk.Canvas(master, height=200, width=1200) #評価ランクの説明を表示するキャンバス
		
		
		# キャンバス表示
		speed.place(x=100, y=50)
		variability.place(x=100, y=250)
		symmetry.place(x=100, y=450)

		speed_point.place(x=500, y=50)
		variability_point.place(x=500, y=250)
		symmetry_point.place(x=500, y=450)

		score.place(x=900, y=50)
		evaluation.place(x=900, y=350)
		index.place(x=100, y=650)

		
		# イメージ作成
		self.img_speed = tk.PhotoImage(file="image/速度.png")
		self.img_variability = tk.PhotoImage(file="image/変動性.png")
		self.img_symmetry = tk.PhotoImage(file="image/対称性.png")

		self.img_speed_point = tk.PhotoImage(file="image/背景.png")
		self.img_variability_point = tk.PhotoImage(file="image/背景.png")
		self.img_symmetry_point = tk.PhotoImage(file="image/背景.png")

		self.img_score = tk.PhotoImage(file="image/総合点.png")
		self.img_evaluation = tk.PhotoImage(file="image/総合評価.png")
		self.img_index = tk.PhotoImage(file="image/評価ランク.png")


		# キャンバスにイメージを表示
		speed.create_image(10, 2, image=self.img_speed, anchor=tk.NW)
		variability.create_image(10, 2, image=self.img_variability, anchor=tk.NW)
		symmetry.create_image(10, 2, image=self.img_symmetry, anchor=tk.NW)

		speed_point.create_image(-15, 2, image=self.img_speed_point, anchor=tk.NW)
		variability_point.create_image(-15, 2, image=self.img_speed_point, anchor=tk.NW)
		symmetry_point.create_image(-15, 2, image=self.img_speed_point, anchor=tk.NW)

		score.create_image(0, 5, image=self.img_score, anchor=tk.NW)
		evaluation.create_image(0, 5, image=self.img_evaluation, anchor=tk.NW)
		index.create_image(10, 2, image=self.img_index, anchor=tk.NW)
		
		
		#結果のファイルを読み込み
		file = open('result.txt', 'r', encoding='UTF-8')
		datalist = file.readlines()
		

		# 点数を生成・表示
		speed_lbl = tk.Label(text=datalist[0].replace("\n", ""), foreground='#1E90FF',background="#B0E2FF", font=("メイリオ",128,"bold"), height=1, width=3, anchor=tk.CENTER) 
		speed_lbl.place(x=560, y=70)
		variability_lbl = tk.Label(text=datalist[1].replace("\n", ""), foreground='#1E90FF',background="#B0E2FF", font=("メイリオ",128,"bold"), height=1, width=3, anchor=tk.CENTER) 
		variability_lbl.place(x=560, y=270)
		symmetry_lbl = tk.Label(text=datalist[2].replace("\n", ""), foreground='#1E90FF',background="#B0E2FF", font=("メイリオ",128,"bold"), height=1, width=3, anchor=tk.CENTER) 
		symmetry_lbl.place(x=560, y=470)

		score_lbl = tk.Label(text=datalist[3].replace("\n", ""), foreground='#FF8247', font=("メイリオ",128,"bold"), height=1, width=3, anchor=tk.CENTER) 
		score_lbl.place(x=970, y=150)
		evaluation_lbl = tk.Label(text=datalist[4].replace("\n", ""), foreground='#FF8247', font=("メイリオ",128,"bold"), height=1, width=3, anchor=tk.CENTER) 
		evaluation_lbl.place(x=970, y=450)

		
def create_win():
	win = tk.Tk()
	app = Application(master=win)
	app.mainloop()
	
	
if __name__ == "__main__":
	create_win()