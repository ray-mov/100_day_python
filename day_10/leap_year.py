def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    isLeapYear = False
    if year%4 == 0:
        isLeapYear = True
    if year%100 == 0:
        isLeapYear = False
    if year%400 == 0:
        isLeapYear = True
    
    return isLeapYear

print(is_leap_year(2000))


# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False