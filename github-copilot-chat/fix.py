def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum inside function:", total)

if __name__ == "__main__":
    # サンプルデータ
    numbers = [1, 2, 3, 4, 5]

    # 合計値を計算
    calculate_sum(numbers)

    # バグ：変数totalは関数内で定義されているため、関数外からアクセスできない
    print("Sum outside function:", total)
    