import random


def daice():
    surface_num = int(input("サイコロの面の数は?: "))
    number_of_times = int(input("何回振りますか?: "))
    # print(surface_num)
    # print(type(int(number_of_times)))
    results = []
    for i in range(number_of_times):
        daice_nam = random.randint(1, surface_num)
        results.append(daice_nam)
    print(results)


daice()
