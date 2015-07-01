import datetime
from django.http import JsonResponse
from django.views.generic import View
from business.models import DefaultCategoryService

class CalcFinalDateView(View):

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        default_category_id = request.GET.get('default_category_id')
        employees_list_id = request.GET.get('employees_list_id')
        area = request.GET.get('area')
        start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        square_feet = DefaultCategoryService.objects.get(pk=int(default_category_id)).score_feet or 1
        quant_employees = int(employees_list_id)
        quant_area = int(area)

        quant_days = (quant_area / square_feet) / quant_employees
        end_date = (start_datetime + datetime.timedelta(days=quant_days)).date()

        return JsonResponse({'end_date': end_date})
