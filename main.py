import MeCab

mecab = MeCab.Tagger('-d /usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd')

text = "あしたハ 〜ハッシュドポテト食べて面接頑張ろウ🤤🖤✌🏿️緊張。"

mecab.parse("") # 文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    # 単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word,pos))
    #次の単語にすすめる
    node = node.next
