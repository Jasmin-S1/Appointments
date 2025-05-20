import calendar
from datetime import datetime

def get_current_week():
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    weeks = calendar.monthcalendar(current_year, current_month)
    for index, sublist in enumerate(weeks):
        if current_day in sublist:
            return index + 1, len(weeks)




