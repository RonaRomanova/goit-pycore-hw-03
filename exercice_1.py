# Завдання 1

# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

from datetime import datetime
date = input("Enter a date (YYYY-MM-DD): ")


def get_days_from_today(date):
    try:
        today = datetime.today()
        input_date = datetime.strptime(date, "%Y-%m-%d")
        delta = today.toordinal()-input_date.toordinal()
        return delta
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

print(get_days_from_today(date))