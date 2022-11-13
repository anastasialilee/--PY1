def get_unique_list_numbers(n=15) -> list[int]:
    import random
    list_ = random.sample(range(-10, 10), n)
    return list_
    # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers(15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
