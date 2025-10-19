from datetime import datetime, timedelta


DATE_FORMAT = "%Y-%m-%d"
EXIT_COMMAND = "E"

"""
    Calculate the number of days between current date and input_date. 
    If input_date is in the future, the result will be negative.
    Args:
        input_date (str): date string in format 'YYYY-MM-DD' e.g. '2020-10-09'. Other formats are not allowed
    Returns:
        int: number of days between input_date and current date
"""
def get_days_from_today(input_date: str) -> int:
    today = datetime.today()
    parsed = datetime.strptime(input_date, DATE_FORMAT)
        
    return (today - parsed).days;

while True:
    try:
        user_input = input("Please enter the date in format 'YYYY-MM-DD'. To exit type E: ")
        if user_input.upper() == EXIT_COMMAND:
            break
        result = get_days_from_today(user_input)
        print(f"Days between current date and input: {result}")
    except ValueError as ex:
        print("Please enter a date in valid format e.g. '2020-10-09'")
        continue
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        continue

assert get_days_from_today(str((datetime.today() + timedelta(days=-3)).strftime(DATE_FORMAT))) == 3, "Valid date in the past should return result"    
assert get_days_from_today(str((datetime.today() + timedelta(days=3)).strftime(DATE_FORMAT))) < 0, "Date in future should return a negative number"
assert get_days_from_today(str(datetime.today().strftime(DATE_FORMAT))) == 0, "Current date should return 0"
try:
    get_days_from_today("")
    assert False, "Invalid input should raise ValueError"
except ValueError:
    pass