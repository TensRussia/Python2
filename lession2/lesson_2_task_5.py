def month_to_season(month):
    if 0 < month <= 2 or month == 12:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "В году месяцы с 1 по 12"


print(month_to_season(1))
print(month_to_season(2))
print(month_to_season(3))
print(month_to_season(4))
print(month_to_season(5))
print(month_to_season(6))
print(month_to_season(7))
print(month_to_season(8))
print(month_to_season(9))
print(month_to_season(10))
print(month_to_season(11))
print(month_to_season(12))
print(month_to_season(13))
print(month_to_season(0))
