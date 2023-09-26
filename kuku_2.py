def main():
    # 1から9までの数字でループする
    for i in range(1, lines + 1):
        # 内部のループも1から9まで
        for j in range(1, columns + 1):
            print(i * j, end=" ")  # 九九の計算結果を出力
        print()  # 次の行へ移動


lines = int(input("行数を入力してください: "))
# print(lines)
columns = int(input("行数を入力してください: "))
# print(columns)

if __name__ == "__main__":
    main()
