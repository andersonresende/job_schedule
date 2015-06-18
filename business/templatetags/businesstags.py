from django import template
from business.models import Service, Holiday

register = template.Library()

def _get_urgency_status(occurrence):
    """
    That function get a occurrence with one event
    and returns the urgency of Service.

    :param occurrence: Occurrence
    :return: String
    """
    event = occurrence.event
    service = Service.objects.get(pk=event.pk)
    urgency = service.urgency_status

    return urgency

def check_is_sunday(day):
    """
    That function get a day and checks if is a sunday.

    :param day: class Day
    :return: Boolean
    """

    return day.start.weekday() == 6

def check_is_holiday(day):
    """
    That function get a day and check if is a holiday and not a work day.

    :param day: class Day
    :return: Boolean
    """

    holiday_lst = Holiday.objects.filter(work_day=False)
    holiday_dates = (holiday.date for holiday in holiday_lst)
    day_date = day.start.date()

    return day_date in holiday_dates

@register.filter
def filter_occurrences_by_urgency(lst, day):
    """
    That function get a list of dicts of occurrence and filter that
    list to show at calendar by event urgency.

    Urgency is normal: show only util days
    Urgency is high: show too on sundays
    Urgency is critical: show all days

    :param lst: List of Occurrence Dict
    :param day: class Day
    :return: List of Occurrence Dict
    """

    final_lst = []
    for dic in lst:
        occurrence = dic['occurrence']
        urgency = _get_urgency_status(occurrence)
        if urgency == Service.NORMAL:
            if not check_is_sunday(day) and not check_is_holiday(day):
                final_lst.append(dic)
        elif urgency == Service.HIGH:
            if not check_is_holiday(day):
                final_lst.append(dic)
        else:
            final_lst.append(dic)

    return final_lst
