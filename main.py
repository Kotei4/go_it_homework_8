from collections import defaultdict
from datetime import date, timedelta, datetime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_birthdays_per_week(users):
    today = date.today()
    def_week = defaultdict(list)

    for user in users:
        birthday = user['birthday']

        if birthday.month == 1 and today.month == 12 and today.day > 25:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year)

        if 0 <= (birthday - today).days < 7:
            if birthday.weekday() == 5:
                birthday = birthday + timedelta(days=2)
            if birthday.weekday() == 6:
                birthday = birthday + timedelta(days=1)

            def_week[weekdays[birthday.weekday()]].append(user['name'].split()[0])

    return def_week


if __name__ == "__main__":
    users = [
        {"name": "John Tyler", "birthday": datetime(1990, 11, 12).date()},
        {"name": "Jan KoumAndrew Jackson", "birthday": datetime(1993, 11, 13).date()},
        {"name": "Martin Van Buren", "birthday": datetime(1990, 11, 14).date()},
        {"name": "William Henry Harrison", "birthday": datetime(1983, 11, 15).date()},
        {"name": "James K. Polk", "birthday": datetime(1985, 11, 16).date()},
        {"name": "Zachary Taylor", "birthday": datetime(1987, 11, 17).date()},
        {"name": "Millard Fillmore", "birthday": datetime(1987, 11, 18).date()},
        {"name": "Bill Gates ", "birthday": datetime(1989, 11, 19).date()},
        {"name": "Jan Clod Van Dam", "birthday": datetime(1988, 11, 20).date()},
        {"name": "Chuck Noris", "birthday": datetime(1985, 11, 21).date()},
        {"name": "Silvester Stalone", "birthday": datetime(1986, 11, 22).date()},
        {"name": "Vin Diesel", "birthday": datetime(1987, 11, 23).date()},
    ]

    result = get_birthdays_per_week(users)
    for day_name, names in result.items():
        print(f'{day_name}: {", ".join(names)}')
