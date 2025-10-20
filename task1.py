from datetime import datetime, timedelta


DATE_FORMAT = "%Y-%m-%d"
EXIT_COMMAND = "E"

"""
    Calculate the number of days between current date and input_date. 
    If input_date is in the future, the result will be negative.
    Args:
        input_date (str): date string in format 'YYYY-MM-DD' e.g. '2020-10-09'. Other formats are not supported
    Returns:
        int: number of days between input_date and current date. If input_date is invalid, return None.
"""
def get_days_from_today(input_date: str) -> int:
    try:
        parsed = datetime.strptime(input_date, DATE_FORMAT)
        today = datetime.today()
    except ValueError:
        return None
    
    return (today - parsed).days;

while True:
    user_input = input("Please enter the date in format 'YYYY-MM-DD'. To exit type E: ")
    if user_input.upper() == EXIT_COMMAND:
        break
    result = get_days_from_today(user_input)
    if result is None:
        print("Invalid date format. Please try again.")
    else: 
        print(f"Days between current date and input: {result}")

assert get_days_from_today(str((datetime.today() + timedelta(days=-3)).strftime(DATE_FORMAT))) == 3, "Valid date in the past should return result"    
assert get_days_from_today(str((datetime.today() + timedelta(days=3)).strftime(DATE_FORMAT))) < 0, "Date in future should return a negative number"
assert get_days_from_today(str(datetime.today().strftime(DATE_FORMAT))) == 0, "Current date should return 0"
assert get_days_from_today("") is None, "Invalid date should return None"