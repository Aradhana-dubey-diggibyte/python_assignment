import calendar

def find_day(month: int, day: int, year: int) -> str:
    
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index].upper()
