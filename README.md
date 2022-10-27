<img src="https://coco-senior.jp/M2kRW38c/wp-content/uploads/2021/05/%E5%A7%BF%E5%8B%A2%E3%81%8C%E6%82%AA%E3%81%8F%E6%AD%A9%E8%A1%8C%E3%81%AB%E4%B8%8D%E5%AE%89%E3%81%AE%E3%81%82%E3%82%8B%E9%AB%98%E9%BD%A2%E5%A5%B3%E6%80%A7%E3%81%AE%E5%86%99%E7%9C%9F.jpeg" height="300">

# independent_project 
## 実行するプログラム
- complement.py：Openposeの.jsonをcsv化，各指標の計算，result.txtの出力を行う．最初に実行する．
- plot_win.py：result.txtの出力をグラフィカルに行う．complement.pyの後に実行する．

> **Note**
> 基本的に上記2つのプログラムだけを実行するようにしてください．

## 実行しないプログラム
- JSONtoCSV：jsonをcsvに変更するプログラム．complement.pyを実行すると自動で実行される．
- sample：complement.pyを実行後sampleと打つと簡単な結果（sora氏のデータ）が見られます．
- image：plot_win.py用の画像が入ったフォルダ．
- requirements.txt：必要なライブラリが記載されたテキストファイル．  

> **Warning**
> requirements.txtには不要なライブラリも記載されています．適宜抽出してください．

## Dependency
requirements.txtを参考にしてください．

## Setup
1. git cloneでローカルに複製． 
```console
git clone git@github.com:mio1717/independent_project.git
```  
```console
git clone https://github.com/mio1717/independent_project.git
```

> **Note**
> 上記の**どちらかのコマンド**を実行してください．git環境が無い方は，Download ZIPをしてください．

2. 必要なライブラリをインストール．
```console
pip install -r requirements.txt  
```
以上でセットアップ完了です．

## Usage
1. complement.pyを実行．
2. 実行の際にフォルダ名を聞かれるので，解析したい被験者のフォルダ名を入力．
> **Warning**
> 解析したい被験者の**フォルダ**はcomplement.pyと**同じディレクトリ**にしてください．フォルダの名前は何でも良いですが，sub1等わかりやすい名前が推奨されます．
3. 実行すると，ターミナルに簡単な解析結果が出力され，解析に利用したフォルダ内にresult.txtが出力される．
4. plot_win.pyを実行．
5. 結果を表示をクリック．
6. 解析に利用したフォルダ内に存在するresult.txtを選択する．  

## Tech
Openpose，Python3

## Authors
M2：ik，sora，eureka，bobobo
B2：reon

## References
https://www.creact.co.jp/wp-content/uploads/2019/04/Gait_Analyser_%E6%AD%A9%E8%A1%8C%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%AE%E8%A9%B3%E8%BF%B0.pdf
