def common_elements():
    # Створення множин чисел, кратних 3 і 5
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}

    # Знаходження перетину двох множин
    intersection_set = multiples_of_3 & multiples_of_5

    # Повернення результату
    return intersection_set
print(common_elements())

