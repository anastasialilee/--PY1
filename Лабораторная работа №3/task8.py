money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
balance = money_capital - spend
spending = 0
while balance + spending >= 0:
    month = month + 1
    spending = salary - spend
    spend = spend * 1.05
    balance = balance + spending
print(month)
