import datetime
from django.http import JsonResponse
from django.views.generic import View
from .models import DefaultCategoryService
from .utils import is_holiday, is_sunday


class CalcFinalDateView(View):

    @staticmethod
    def increment_date(start_datetime, quant_days, urgency_status):
        """
        That function returns a new datetime evaluetade by others parameters.
        if urgency == 'NO' -> increment a more day on sundays and holidays
           urgency == 'HG' -> increment a more day on holidays
        else return the same Datetime received.

        :param start_datetime: Datetime
        :param quant_days: Int
        :param urgency_status: String
        :return: Datetime
        """

        end_datetime = start_datetime
        one_day = datetime.timedelta(days=1)
        if urgency_status == 'NO':
            for _ in range(quant_days):
                end_datetime = end_datetime + one_day
                while is_sunday(end_datetime) or is_holiday(end_datetime):
                    end_datetime += one_day
        elif urgency_status == 'HI':
            for _ in range(quant_days):
                end_datetime = end_datetime + one_day
                while is_holiday(end_datetime):
                    end_datetime += one_day
        else:
            end_datetime = end_datetime + datetime.timedelta(days=quant_days)

        return end_datetime.date()

    @staticmethod
    def calc_quant_days(quant_area, square_feet, quant_employees):
        """
        That function calculate a quant of days by other parameters
        using one math formula.

        :param quant_area: Int
        :param square_feet: Int
        :param quant_employees: Int
        :return: Int
        """

        quant_days = (quant_area / square_feet) / quant_employees
        return quant_days

    def get(self, request, *args, **kwargs):

        # receive data from request
        start_date = request.GET.get('start_date')
        default_category_id = request.GET.get('default_category_id')
        employees_list_id = request.GET.get('employees_list_id')
        area = request.GET.get('area')
        urgency_status = request.GET.get('urgency_status')

        # convert data to be used on functions
        start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        square_feet = DefaultCategoryService.objects.get(pk=int(default_category_id)).score_feet or 1
        quant_employees = int(employees_list_id)
        quant_area = int(area)

        # get quant of days
        quant_days = self.calc_quant_days(quant_area, square_feet, quant_employees)

        # get a new datetime
        end_date = self.increment_date(start_datetime, quant_days, urgency_status)

        return JsonResponse({'end_date': end_date})






