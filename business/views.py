from django.http import HttpResponse
from django.views.generic import View

class CalcFinalDateView(View):

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        default_category_id = request.GET.get('default_category')
        employees_list_id = request.GET.get('employees_list[]')
        area = request.GET.get('area')

        return HttpResponse('Hello, World!')
