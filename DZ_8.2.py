from datetime import datetime, timedelta

def get_birthdays_per_week(user_list):
    date_now = datetime.now()
    birthdays_by_weekday = {}
    
    for user in user_list:
        birthday = user["birthday"]
        
        if (
            birthday.month == date_now.month
            and birthday.day >= date_now.day
            and birthday.day <= date_now.day + 7
        ):
            birthday_now = datetime(date_now.year, birthday.month, birthday.day)
            
            if birthday_now.weekday() == 5:  # Saturday
                birthday_now += timedelta(days=2)
            elif birthday_now.weekday() == 6:  # Sunday
                birthday_now += timedelta(days=1)
            
            if (
                birthday_now.month == date_now.month
                and birthday_now.day >= date_now.day
                and birthday_now.day <= date_now.day + 7
            ):
                weekday = birthday_now.strftime('%A')
                
                if weekday not in birthdays_by_weekday:
                    birthdays_by_weekday[weekday] = []
                
                birthdays_by_weekday[weekday].append(user["name"])
    
    for weekday, birthdays in sorted(birthdays_by_weekday.items()):
        birthday_list = ", ".join(birthdays)
        print(f"{weekday}: {birthday_list}")


users = [
    {"name": "John", "birthday": datetime(1990, 6, 5)},
    {"name": "Alice", "birthday": datetime(1995, 6, 6)},
    {"name": "David", "birthday": datetime(1987, 6, 7)},
    {"name": "Bill", "birthday": datetime(1992, 6, 8)},
    {"name": "Jill", "birthday": datetime(1994, 6, 9)},
    {"name": "Kim", "birthday": datetime(1991, 6, 5)},
    {"name": "Jan", "birthday": datetime(1988, 6, 11)},
]

get_birthdays_per_week(users)
