'''
Завдання 4
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

Вимоги до завдання:
Параметр функції users — це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
'''
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    '''
    Визначає, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
    '''
    upcoming_birthdays = []
    today = datetime.today().date()
    
    for user in users:
        name = user['name']
        birthday_str = user['birthday']
        birthday_date = datetime.strptime(birthday_str, '%Y.%m.%d').date()
        
    # Визначаємо дату наступного дня народження
        next_birthday = birthday_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        
        # Перевіряємо, чи день народження випадає в межах наступних 7 днів
        if today <= next_birthday <= today + timedelta(days=7):
            congratulation_date = next_birthday
            # Якщо день народження припадає на вихідний, переносимо на наступний понеділок
            if congratulation_date.weekday() >= 5:  # 5 - субота, 6 - неділя
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
            
            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.03.21"},
    {"name": "Jane Smith", "birthday": "1990.03.12"},
    {"name": "Nadiia Romanova", "birthday": "1990.03.15"},
    {"name": "Alice Johnson", "birthday": "1988.03.18"},
    {"name": "Bob Brown", "birthday": "1992.03.09"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("List of upcoming birthdays:", upcoming_birthdays)