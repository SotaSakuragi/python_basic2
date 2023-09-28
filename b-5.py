"""
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
"""


def get_numbers():
    numbers = input("データを入力してください(スペース区切り) > ")
    return [int(num) for num in numbers.split()]


def calculate_sum(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total


def calculate_min(numbers_list):
    min_value = numbers_list[0]
    for num in numbers_list[1:]:
        if num < min_value:
            min_value = num
    return min_value


def calculate_max(numbers_list):
    max_value = numbers_list[0]
    for num in numbers_list[1:]:
        if num > max_value:
            max_value = num
    return max_value


def calculate_average(numbers_list):
    total = calculate_sum(numbers_list)
    count = 0
    for _ in numbers_list:
        count += 1
    return total // count


def calculator():
    numbers_list = get_numbers()

    print(f"合計値: {calculate_sum(numbers_list)}")
    print(f"最大値: {calculate_max(numbers_list)}")
    print(f"最小値: {calculate_min(numbers_list)}")
    print(f"平均値: {calculate_average(numbers_list)}")


calculator()
