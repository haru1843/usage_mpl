# はじめに
matplotlibをデフォルトで利用し, 軸ラベルやテキスト挿入時に日本語を用いると, 文字化けしてしまいます.


# 対処
以下のように日本語対応のフォントを設定します.

```python
font = {"family": "IPAexGothic"}
mpl.rc('font', **font)
```

また, これらのフォントが入っていない場合, インストールする必要があります.

# 例
7,8行目でフォントの設定がなされています.

@import "./japanese.py" {cmd="python3" matplotlib=true class=line-numbers}