"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
"""
def makes_twenty(number_one: int, number_two: int):
    if number_one == 20 or number_two == 20:
        return True
    elif number_one + number_two == 20:
        return True
    else:
        return False

result = makes_twenty(10, 10)
print(result)
    