def is_year_leap(year):
    if year % 4 == 0:
        return True
    return False


year11 = 2022
result = is_year_leap(year11)
print(f"год {year11}: {result}")
year11 = 2024
result = is_year_leap(year11)
print(f"год {year11}: {result}")
