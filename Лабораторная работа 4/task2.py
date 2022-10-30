def get_count_char(str_):
    str_with_lower = str_.lower()
    list_ = str_with_lower.split()
    first_str = ''.join(list_)
    first_list = first_str.split('!')
    second_str = ''.join(first_list)
    second_list = second_str.split('.')
    third_str = ''.join(second_list)
    third_list = third_str.split(',')
    s_str = ''.join(third_list)
    set_str = {}
    count = 0
    for a in s_str:
        if a in set_str:
            set_str[a] += 1
        else:
            set_str[a] = 1
    return set_str


 # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
