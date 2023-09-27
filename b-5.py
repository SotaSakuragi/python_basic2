def calculator():
    numbers = input("データを入力してください(スペース区切り) > ")
    sum_numbers_list = 0
    numbers_list = []
    for num in numbers.split():
        numbers_list.append(int(num))
    # print(numbers_list)

    for i in numbers_list:
        sum_numbers_list += i
    print(f"合計値: {sum_numbers_list}")

    # print(sum(numbers_list))
    # print(min(numbers_list))
    # print(max(numbers_list))
    # print(sum(numbers_list) / len(numbers_list))

    min_value = numbers_list[0]
    max_value = numbers_list[0]

    for num in numbers_list[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    print(f"最大値: {max_value}")
    print(f"最小値: {min_value}")

    count = 0
    for j in numbers_list:
        count += 1
    # print(f"確認{count}")

    print(f"平均値: {sum_numbers_list // count}")


calculator()
