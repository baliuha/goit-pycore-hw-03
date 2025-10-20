import random


"""
    Generate a sorted list of unique random numbers within a specified range.
    Args:
        min (int): minimum possible number in the set (not less than 1)
        max (int): maximum possible number in the set (not more than 1000)
        quantity (int): quantity of numbers to pick
    Returns:
        list[int]: sorted list of randomly picked unique numbers. If parameters do not meet the constraints, return an empty list.
"""
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not (1 <= min <= max <= 1000) or (max - min + 1 < quantity):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6) 
print("Your lottery numbers:", lottery_numbers)

assert len(get_numbers_ticket(10, 50, 20)) == 20, "Should return 20 unique numbers"
assert len(get_numbers_ticket(1, 1000, 1000)) == 1000, "Should return 1000 unique numbers" # basically just a list with values from 1 to 1000
assert get_numbers_ticket(0, 10, 5) == [], "Min value less than allowed should return empty list"
assert get_numbers_ticket(2, 1001, 5) == [], "Max value more than allowed should return empty list"
assert get_numbers_ticket(10, 5, 3) == [], "Min value more than max should return empty list"
assert get_numbers_ticket(10, 15, 7) == [], "Quantity is more then min-max range should return empty list"