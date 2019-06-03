# 対象読者

* C言語はやったことあるけど, 他の言語は…
* オブジェクト指向って何?
* クラスは聞いたことがない or 使ったことがない

という人向けです. まったくプログラムを習ったことがない人向けではないのでご注意ください.

# コンセプト

まずはじめに「クラスとはどんなものか」という話をしてからPythonの内容に移りたいと思います.

また, Pythonの文法の部分は以下のサイクルで進めていきたいと思います.

1. `xxx`というものを作ろう
2. `xxx`はCだとこう書けるよ. → ではPythonでは?
3. Pythonだとこういう書き方があるので, こう書けます.

というのを何サイクルも行い, Pythonの学習を進めていきたいと思います.

# WindowsにおけるPythonの環境構築

もう一つのフォルダ「プログラミング自体初めての人」の方で取り上げているので, 環境ができていない人はそちらへ.

# HTMLとPDF
内容は同じです. PDFはページ分割の関係でスタイルが崩れてたり, 見づらかったりするかもしれません.

# リンク

各HTMLファイルを見るときは[こちら](http://htmlpreview.github.io/?)へ飛んでから, 各HTMLファイルのURLをコピペしてあげてください.

一応下に各HTMLファイルのビューワーページへのリンクを貼っておきますが, リンクがきちんと繋がってない場合があるので, ご了承ください.

| 番号 | ファイル名 | リンク |
| :-: | :-: | :-: |
| 00 | Pythonの特徴 | [こちら][0] |
| 01 | クラスとは | [こちら][1] |
| 02 | 変数と方と演算子 | [こちら][2] |
| 03 | 便利なメソッドなど | [こちら][3] |
| 04 | 構文 | [こちら][4] |
| 05 | 関数とスコープ | [こちら][5] |
| 06 | パッケージやモジュールのインポート | [こちら][6] |
| 07 | --- | --- [こちら][7] |
| 08 | 便利なビルトイン関数 | [こちら][8] |
| -- | --- | -- |
| 99 | 命名規則とコーディング規則 | [こちら][99] |

[0]:http://htmlpreview.github.io/?=
[1]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/01_%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%A8%E3%81%AF.html
[2]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/02_%E5%A4%89%E6%95%B0%E3%81%A8%E5%9E%8B%E3%81%A8%E6%BC%94%E7%AE%97%E5%AD%90.html
[3]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/03_%E4%BE%BF%E5%88%A9%E3%81%AA%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E3%81%AA%E3%81%A9.html
[4]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/04_%E6%A7%8B%E6%96%87.html
[5]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/05_%E9%96%A2%E6%95%B0%E3%81%A8%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97.html
[6]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/06_%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%82%84%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88.html
<!-- [7]:http://htmlpreview.github.io/? -->
[8]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/08_%E4%BE%BF%E5%88%A9%E3%81%AA%E3%83%93%E3%83%AB%E3%83%88%E3%82%A4%E3%83%B3%E9%96%A2%E6%95%B0.html

[99]:http://htmlpreview.github.io/?https://github.com/haru1843/usage_mpl/blob/master/python%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/C%E8%A8%80%E8%AA%9E%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91/99_%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87%E3%81%A8%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E8%A6%8F%E7%B4%84.html