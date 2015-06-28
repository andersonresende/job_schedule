from django import template
from business.models import Service, Holiday

register = template.Library()

@register.inclusion_tag("schedule/tooltip_info.html", takes_context=True)
def render_tooltip_info(context, dic):
    """
    That function returns de custom tooltip html
    to service.

    :param dic: Dict
    :return: Context
    """
    service = get_service(dic)
    info_dic = service.get_tooltip_info()
    context.update(info_dic)

    return context

def get_service(dic):
    """
    That functions get a occurrence and returns a service
    from occurrence event.

    :param dic: Dict
    :return: Service Obj
    """
    occurrence = dic['occurrence']
    event = occurrence.event
    service = Service.objects.get(pk=event.pk)

    return service

@register.filter
def get_reference(dic):
    """
    That function get a dict with occurrence obj and return
    the reference of occurrence service.

    :param dic: Dict
    :return: String
    """

    service = get_service(dic)
    reference = service.reference

    return reference

@register.filter
def get_color_service(dic):
    """
    That functions get a dict with occurence obj and return the
    color of occurrence service.

    :param dic: Dict
    :return: String
    """

    service = get_service(dic)
    color = service.get_color()

    return color

def _get_urgency_status(dic):
    """
    That function get a occurrence with one event
    and returns the urgency of Service.

    :param dic: Dict
    :return: String
    """
    service = get_service(dic)
    urgency = service.urgency_status

    return urgency

@register.filter
def check_is_sunday(day):
    """
    That function get a day and checks if is a sunday.

    :param day: class Day
    :return: Boolean
    """

    return day.start.weekday() == 6

@register.filter
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
    list to show at calendar by service urgency.

    Urgency is normal: show only util days
    Urgency is high: show too on sundays
    Urgency is critical: show all days

    :param lst: List of Occurrence Dict
    :param day: class Day
    :return: List of Occurrence Dict
    """

    final_lst = []
    for dic in lst:
        urgency = _get_urgency_status(dic)
        if urgency == Service.NORMAL:
            if not check_is_sunday(day) and not check_is_holiday(day):
                final_lst.append(dic)
        elif urgency == Service.HIGH:
            if not check_is_holiday(day):
                final_lst.append(dic)
        else:
            final_lst.append(dic)

    return final_lst
