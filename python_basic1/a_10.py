# A-10: サイコロ
# 下記のコードが期待通り動作するような、dice() 関数を実装してください ※ dice()関数は1から6の整数をランダムに返す(Day2のおみくじアプリで使ったrandomモジュールを使います)
# dice()

# import random
# dice = ["1", "2", "3", "4", "5", "6"]
# rint(random.choice(dice))

import random

def dice():
    n = [1, 2, 3, 4, 5, 6]
    return random.choice(n)

print(dice())
