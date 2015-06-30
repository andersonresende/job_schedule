from django.db import models
from colorful.fields import RGBColorField
from schedule.models.events import Event


class CategoryEmployee(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    medal = models.ImageField(upload_to='business', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category Employee'
        verbose_name_plural = 'Category Employees'


class Employee(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    category_employee = models.ForeignKey(CategoryEmployee, related_name='employees')

    def __unicode__(self):
        return self.name

    def get_medal(self):
        """
        That function returns a medal from category employee.

        :return: ImageField
        """

        return self.category_employee.medal

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class CategoryService(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    color = RGBColorField()

    def __unicode__(self):
        return self.name

    def get_color(self):
        return self.color

    class Meta:
        verbose_name = 'Category Service'
        verbose_name_plural = 'Category Services'
        abstract = True


class DefaultCategoryService(CategoryService):
    score_feet = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Default Category Service'
        verbose_name_plural = 'Default Category Services'


class CustomCategoryService(CategoryService):
    class Meta:
        verbose_name = 'Custom Category Service'
        verbose_name_plural = 'Custom Category Services'


class Service(Event):
    NORMAL = 'NO'
    HIGH = 'HI'
    CRITICAL = 'CT'
    URGENCY_STATUS_CHOICES = (
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )
    reference = models.CharField(max_length=750, null=True, blank=True)
    default_category_service = models.ForeignKey(
        DefaultCategoryService,
        related_name='services',
        null=True,
        blank=True
    )
    custom_category_service = models.OneToOneField(
        CustomCategoryService,
        related_name='service',
        null=True,
        blank=True
    )
    employees = models.ManyToManyField(Employee, related_name='services')
    urgency_status = models.CharField(max_length=2, choices=URGENCY_STATUS_CHOICES, default=NORMAL)
    area = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_category_service(self):
        """
        That functions returns the category_service seted.

        :return: obj subclass of CategoryService
        """

        return self.default_category_service or self.custom_category_service

    def get_color(self):
        """
        That function check what service exists and return your rgb color.

        :return: String
        """

        category_service = self.get_category_service()
        return category_service.get_color()

    def get_tooltip_info(self):
        """
        That function returns tooltip info to be used on render template.

        :return: Dict
        """

        dic = {
            'title': self.title,
            'category_service': self.get_category_service(),
            'start_date': str(self.start.date()),
            'end_date': str(self.end.date()),
            'employees': self.employees.all(),
        }

        return dic

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Holiday(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    date = models.DateField()
    work_day = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Holiday'
        verbose_name_plural = 'Holidays'

