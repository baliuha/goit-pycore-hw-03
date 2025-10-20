import re


"""
    Normalize phone number to the format +380XXXXXXXXX
    Args:
        phone_number (str): phone number in various formats
    Returns:
        str: normalized phone number in the format +380XXXXXXXXX
"""
def normalize_phone(phone_number: str) -> str:
    # matches any char that is not a digit or + at the start
    normalized = re.sub(r"[^\d+]|(?<=.)\+", "", phone_number) 

    if normalized.startswith("+"):
        return normalized
    else:
        return "+" + normalized if normalized.startswith('380') else '+38' + normalized

input_data = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234", 
    "(050)88899+00", # modified example to add case with + in the middle
    "38050-111-22-22",
    "38050 111 22 11   ",
]
expected_result = [
    '+380671234567',
    '+380952345678',
    '+380441234567',
    '+380501234567',
    '+380501233234',
    '+380503451234',
    '+380508889900',
    '+380501112222',
    '+380501112211',
]
actual_result = [normalize_phone(num) for num in input_data]

assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"