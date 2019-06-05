# 各ファイルの説明

| 順番 | ファイル名 | 内容/備考 |
| :-: | :-: | :-: |
| 00 | python3とは | python3の周辺知識について. <br>「プログラミングをする上で最低限知っておいて欲しい知識」と<br>「python3と他の言語の違い」についてのべています. |
| 01 | 環境の導入 | windowsにおいてpython3の環境を整える手段をまとめています. |
| 02 | 動かしてみよう | python3で「こんにちは, 世界!」をします. |
| 03 | 変数と型 | 変数の仕組みとpythonでよく使われる型を紹介します. |
| 04 | リストやタプル | シーケンス型の使い方を示しています. |

# 読み進め方
やる気がある人は00から順に読み進めていってください.  
内容は少し難しい部分があるかもしれませんが, そういうところは遠慮なく飛ばして大丈夫です.  

また, 06や07に関しては, ひょっとしたら飛ばしても良いかもしれません.  

数字の大きい, 90番代のものは, 興味がある人向けのもので, pythonに関係してないものも多く含みます. こちらは完全に読まなくても大丈夫です.  

# 各ファイルのHTMLのプレビューのリンク

| 順番 | ファイル名 | リンク |
| :-: | :-: | :-: |
| 00 | python3とは |  |
| 01 | 環境の導入 | 1.[pythonの導入][1-1], 2.[numpyとmplの導入][1-2], その他[pipとは][1-pip] |
| 02 | 動かしてみよう | [こちら][2] |
| 03 | 変数と型 | [こちら][3] |
| 04 | リストやタプル | [こちら][4] |
| 05 | 演算子 | [こちら][5] |
| 06 | 関数 | [こちら][6] |
| 07 | クラスの簡単な説明 | [こちら][7] |
| 08 | 各型のメソッドとメンバ | [こちら][8] |
| 09 | 構文 | [こちら][9] |
<!-- | n | --- | [こちら][6] | -->


[1-1]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/01_%E7%92%B0%E5%A2%83%E3%81%AE%E5%B0%8E%E5%85%A5/python%E3%81%AE%E5%B0%8E%E5%85%A5.html

[1-2]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/01_%E7%92%B0%E5%A2%83%E3%81%AE%E5%B0%8E%E5%85%A5/numpy%E3%81%A8matplotlib%E3%81%AE%E5%B0%8E%E5%85%A5.html

[1-pip]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/01_%E7%92%B0%E5%A2%83%E3%81%AE%E5%B0%8E%E5%85%A5/pip%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6.html

[2]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/02_%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86.html

[3]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/03_%E5%A4%89%E6%95%B0%E3%81%A8%E5%9E%8B.html

[4]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/04_%E3%82%B7%E3%83%BC%E3%82%B1%E3%83%B3%E3%82%B9%E3%81%A8%E3%83%9E%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E5%9E%8B.html

[5]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/05_%E6%BC%94%E7%AE%97%E5%AD%90.html

[6]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/06_%E9%96%A2%E6%95%B0.html

[7]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/07_%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AE%E7%B0%A1%E5%8D%98%E3%81%AA%E8%AA%AC%E6%98%8E.html

[8]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/08_%E5%90%84%E5%9E%8B%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E3%81%A8%E3%83%A1%E3%83%B3%E3%83%90.html

[9]:http://htmlpreview.github.com/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%87%AA%E4%BD%93%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AE%E4%BA%BA/09_%E6%A7%8B%E6%96%87.html

[10]:http://htmlpreview.github.com/?


<!-- http://htmlpreview.github.com/? -->