def main():
    # 1からlinesまでの数字でループする
    for i in range(1, lines + 1):
        # 内部のループも1からcolumnsまで
        for j in range(1, columns + 1):
            # 九九の計算結果を求める
            result = i * j

            # 桁数に応じたスペースを計算する
            if result < 10:  # 一桁の場合
                space = " "
            elif result < 100:  # 二桁の場合
                space = ""

            # f-stringを使用して、整形した結果を出力
            print(f"{i} x {j} = {space}{result}", end=" |")
        print()  # 次の行へ移動


lines = int(input("行数を入力してください: "))
# print(lines)
columns = int(input("行数を入力してください: "))
# print(columns)

if __name__ == "__main__":
    main()
