import calendar
from datetime import datetime, date, timedelta


def should_move_leap_birthday(birthday_date: datetime.date, current_year: int) -> bool:
    return birthday_date.month == 2 and birthday_date.day == 29 and not calendar.isleap(current_year);

# Move the date to the next Monday if it falls on a weekend
def move_date_to_monday(congrats_date: datetime.date) -> datetime.date:
    if congrats_date.weekday() == 5:  # Saturday
        congrats_date += timedelta(days=2)
    elif congrats_date.weekday() == 6:  # Sunday
        congrats_date += timedelta(days=1)

    return congrats_date

"""
    Get upcoming birthdays within the next 7 days including current date.
    If birthday falls on weekend, move the congratulation date to the next Monday.
    Args:
        users (list[dict]): list of users as dictionaries with user names and birthdays in format 'year.month.day'
    Returns:
        list[dict]: list of users as dictionaries with user names and congratulation dates in format 'year.month.day'
"""
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    one_week_later = today + timedelta(days=7)
    congrats_list = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # edge case 1: leap year birthday
        # when birthday is on Feb 29 and current year is not a leap one, consider birthday as Feb 28
        if should_move_leap_birthday(birthday, today.year):
            birthday_this_year = date(today.year, 2, 28)
        else: 
            birthday_this_year = birthday.replace(year=today.year)

        # edge case 2: year rollover e.g. today = December 29, birthday = January 2 should still count as upcoming
        # if birthday has passed, consider next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= one_week_later:
            congrats_date = move_date_to_monday(birthday_this_year)
            congrats_list.append({
                "name": user["name"],
                "congratulation_date": congrats_date.strftime("%Y.%m.%d")
            })

    return congrats_list

users = [
    {"name": "Satoru Gojo", "birthday": "1990.01.23"},
    {"name": "Suguru Geto", "birthday": "1990.01.27"},
    {"name": "Shoko Ieiri", "birthday": "2024.02.29"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Upcoming birthdays for this week:", upcoming_birthdays)