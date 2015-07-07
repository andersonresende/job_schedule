from django import template
from django.core import urlresolvers
from business.models import Service, Holiday, DefaultCategoryService
from business.utils import is_holiday, is_sunday

register = template.Library()

@register.inclusion_tag("schedule/legend.html", takes_context=True)
def render_legend(context):
    """
    That function returns de legend html to default category
    service.

    :param dic: Dict
    :return: Context
    """
    category_service_lst = DefaultCategoryService.objects.all()
    context.update({'category_service_lst': category_service_lst})
    return context

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
def get_id(dic):
    """
    That function get a dict with occurrence obj and return
    the id of occurrence service.

    :param dic: Dict
    :return: Int
    """

    service = get_service(dic)
    id = service.id

    return id

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
    That function get a day and checks if is a sunday for template.

    :param day: class Day
    :return: Boolean
    """

    return is_sunday(day.start)

@register.filter
def get_holiday_name(day):
    """
    That functions receives one day and returns a holiday name.

    :param day: Day object
    :return: String
    """
    day_date = day.start.date()
    holiday = Holiday.objects.get(date=day_date)

    return holiday.name

@register.filter
def check_is_holiday(day):
    """
    That function get a day and check if is a holiday for template.

    :param day: class Day
    :return: Boolean
    """

    return is_holiday(day.start)

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
