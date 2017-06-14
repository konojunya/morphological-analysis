import MeCab
import glob


def read():
    dirs = glob.glob("/Users/kounojunya/dev/hobby/jk_analysis/tweets/*")
    for item in dirs:
        for path in glob.glob(item + "/*.txt"):
            for f_text in open(path, "r"):
                analysis(f_text)


def analysis(text):
    node = mecab.parseToNode(text)
    while node:
        # 単語を取得
        word = node.surface
        # 品詞を取得
        pos = node.feature.split(",")[1]
        print('{0} , {1}'.format(word, pos))
        # 次の単語にすすめる
        node = node.next


def start():
    read()


if __name__ == "__main__":
    mecab = MeCab.Tagger(
        '-d /usr/local/mecab/lib/mecab/dic/mecab-ipadic-neologd')
    mecab.parse("")  # 文字列がGCされるのを防ぐ

    start()
