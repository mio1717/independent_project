import tkinter as tk
from tkinter.tix import DirSelectDialog
from PIL import Image, ImageTk
import os
import time
import tkinter.filedialog


class Application(tk.Frame):
	
	def __init__(self,master = None):
		super().__init__(master)
		self.pack()
		
		#ウィンドウを大きさ・タイトル
		monitor_height = master.winfo_screenheight() #モニターの高さを取得
		monitor_width = master.winfo_screenwidth() #モニターの幅を取得

		master.geometry(str(monitor_width) + "x" + str(monitor_height)) #横x縦
		master.title("診断結果")

		std_x = (monitor_width-1200)/2 #横が1200より大きい前提
		std_y = (monitor_height-800)/2 #縦が800より大きい前提
		
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
		speed.place(x=std_x, y=std_y+4) #位置が合わなかったので微調整したよ
		variability.place(x=std_x, y=std_y+200)
		symmetry.place(x=std_x, y=std_y+400+2) #位置が合わなかったので微調整したよ

		speed_point.place(x=std_x+400, y=std_y)
		variability_point.place(x=std_x+400, y=std_y+200)
		symmetry_point.place(x=std_x+400, y=std_y+400)

		score.place(x=std_x+800, y=std_y)
		evaluation.place(x=std_x+800, y=std_y+300)
		index.place(x=std_x, y=std_y+600)
		
		# イメージ作成
		self.img_speed = tk.PhotoImage(file="./image/speed.png")
		self.img_variability = tk.PhotoImage(file="./image/variability.png")
		self.img_symmetry = tk.PhotoImage(file="./image/symmetry.png")

		self.img_speed_point = tk.PhotoImage(file="./image/back.png")
		self.img_variability_point = tk.PhotoImage(file="./image/back.png")
		self.img_symmetry_point = tk.PhotoImage(file="./image/back.png")

		self.img_score = tk.PhotoImage(file="./image/total_score.png")
		self.img_evaluation = tk.PhotoImage(file="./image/total_rank.png")
		self.img_index = tk.PhotoImage(file="./image/rating_rank.png")

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
		
		# ボタン作成
		self.btn = tk.Button(master, text='結果を表示', command=lambda:self.btn_click(std_x,std_y))
		self.btn.place(x=monitor_width/2-50, y=monitor_height-std_y)

	# ボタンのクリックイベント
	def btn_click(self,std_x,std_y):
		
		#結果のファイルを読み込み
		filepath = self.dirdialog_clicked()
		file = open(filepath, 'r', encoding='UTF-8')
		datalist = file.readlines()

		# 点数を生成・表示
		score_font = 81
		total_font = 91
		score_x = 490
		total_x = 870 

		self.speed_lbl = tk.Label(text=datalist[0].replace("\n", ""), foreground='#1E90FF',background="#B0E2FF", font=("メイリオ",score_font,"bold"), height=1, width=3, anchor=tk.CENTER) 
		self.speed_lbl.place(x=std_x+score_x, y=std_y+30)
		self.variability_lbl = tk.Label(text=datalist[1].replace("\n", ""), foreground='#1E90FF',background="#B0E2FF", font=("メイリオ",score_font,"bold"), height=1, width=3, anchor=tk.CENTER) 
		self.variability_lbl.place(x=std_x+score_x, y=std_y+230)
		self.symmetry_lbl = tk.Label(text=datalist[2].replace("\n", ""), foreground='#1E90FF',background="#B0E2FF", font=("メイリオ",score_font,"bold"), height=1, width=3, anchor=tk.CENTER) 
		self.symmetry_lbl.place(x=std_x+score_x, y=std_y+430)

		self.score_lbl = tk.Label(text=datalist[3].replace("\n", ""), foreground='#FF8247', font=("メイリオ",total_font,"bold"), height=1, width=3, anchor=tk.CENTER) 
		self.score_lbl.place(x=std_x+total_x, y=std_y+95)
		self.evaluation_lbl = tk.Label(text=datalist[4].replace("\n", ""), foreground='#FF8247', font=("メイリオ",total_font,"bold"), height=1, width=3, anchor=tk.CENTER) 
		self.evaluation_lbl.place(x=std_x+total_x, y=std_y+390)
	
		#数値を変更
		self.speed_lbl['text'] = datalist[0].replace("\n", "")
		self.variability_lbl['text'] = datalist[1].replace("\n", "")
		self.symmetry_lbl['text'] = datalist[2].replace("\n", "")
		self.score_lbl['text'] = datalist[3].replace("\n", "")
		self.evaluation_lbl['text'] = datalist[4].replace("\n", "")

	# フォルダ指定の関数
	def dirdialog_clicked(self):
		filename = tk.filedialog.askopenfilename()
		return filename

		
def create_win():
	win = tk.Tk()
	app = Application(master=win)
	app.mainloop()
	
	
if __name__ == "__main__":
	create_win()