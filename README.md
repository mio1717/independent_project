![image](https://user-images.githubusercontent.com/66098701/197500827-dfa3e8d6-9f7f-4ace-acab-c8d4198c3cec.png)

# independent_project 
学生自主企画研究 使用コード一覧
- complement.py：Openposeの.jsonをcsv化，その後各指標の計算，result.txtの出力を行う．まずはじめにこのコードを実行する．
- plot_win.py：sora氏作成コード．結果の出力を行う．complement.pyの後に実行する．
- JSONtoCSV：jsonをcsvに変更するプログラム．実行する必要はない．
- sample：complement.pyを実行後sampleと打つと簡単な結果（sora氏）が見られます．
- image：plot_win.py用の画像，弄らないでください．
- requirements.py：必要なライブラリ（色々書いてあるので必要なところのみ抜粋してください）

## Dependency
requirements.txtを参考にしてください．

## Setup
1. git cloneでローカルに複製．  
git clone git@github.com:mio1717/independent_project.git  
or  
git clone https://github.com/mio1717/independent_project.git
2. pip install -r requirements.txtで必要なファイルをインストール．  
以上でセットアップ完了です．エラーが出た際は調べた後質問してください．

## Usage
1. Openposeでjsonの入ったファイルを作成．
2. complement.pyを実行．
3. 実行の際にフォルダ名を聞かれるのでフォルダ名を打つ．  
※フォルダは現在のディレクトリの真下においてください．名前は何でも良いですが，sub1など英数字にしておくのが無難です．
5. 実行すると，ターミナルに結果と利用したフォルダ内にresult.txtが出力される．
6. plot_win.pyを実行．実行時にファイルを選択．
7. 結果がグラフィカルに出力される．  

## License
特になし

## Authors
ik,sora,eureka,bobobo,reon

## References
https://www.creact.co.jp/wp-content/uploads/2019/04/Gait_Analyser_%E6%AD%A9%E8%A1%8C%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%AE%E8%A9%B3%E8%BF%B0.pdf
