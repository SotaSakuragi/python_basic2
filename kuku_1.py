# python kuku_1.py


def main():
    # 1から9までの数字でループする
    for i in range(1, 10):
        # 内部のループも1から9まで
        for j in range(1, 10):
            print(i * j, end=" ")  # 九九の計算結果を出力
        print()  # 次の行へ移動


if __name__ == "__main__":
    main()


# print(1, end=" ")
# print(2, end=" ")
# print(3, end=" ")
