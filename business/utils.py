from .models import Holiday

def is_sunday(datetime):
    """
    That functions receives a datetime and check if is saunday.

    :param datetime: Datetime
    :return: Boolean
    """
    return datetime.weekday() == 6

def is_holiday(datetime):
    """
    That function receives a datetime and check is is a work
    holiday.

    :param datetime: Datetime
    :return: Boolean
    """

    holiday_lst = Holiday.objects.filter(work_day=False)
    holiday_dates = (holiday.date for holiday in holiday_lst)
    day_date = datetime.date()

    return day_date in holiday_dates
