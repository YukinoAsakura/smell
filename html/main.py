import pandas as pd
import sounds

lim = []
#エクセルデータでの読み込みになっている
xls_data2 = pd.read_excel('20220421123834_class__PtoP.xls',skiprows=[0,1,2,3])


for row in xls_data2.values:
    lim.append(row)
#データ構造上の匂いデータの数値のみ取り出している
lim2 = lim[1][1:10]

for i in lim2:
    if i > 500:#とりあえず適当な数字上限
        sounds.test()#音声呼び出し
        print("カレーかもしれない")
        break

    elif i <-500:#とりあえず適当な数字下限
        sounds.alert_min()#音声呼び出し
        print("鍋焼うどん")

        break


