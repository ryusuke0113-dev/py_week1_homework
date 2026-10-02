# B-1: 日本の九九表
def create_kuku_table(rows, columns):
    # rows行、columns列の掛け算表を返す
    table = []

    for row in range(1, rows + 1):
        row_data = []

        for column in range(1, columns + 1):
            kuku = row * column
            row_data.append(kuku)

        table.append(row_data)

    return table


def main():
    rows = int(input("行数を入力してください: "))
    columns = int(input("列数を入力してください: "))

    # create_kuku_table() の結果を表示する
    table = create_kuku_table(rows, columns)

    for row in table:
        print(row)

if __name__ == "__main__":
    main()
