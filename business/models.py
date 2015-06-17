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
        verbose_name_plural = 'Category Employees '


class Employee(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    category_employee = models.ForeignKey(CategoryEmployee, related_name='employees')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees '


class CategoryService(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    color = RGBColorField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category Service'
        verbose_name_plural = 'Category Services '


class Service(Event):
    reference = models.CharField(max_length=750, null=True, blank=True)
    category_service = models.ForeignKey(CategoryService, related_name='services')
    employees = models.ManyToManyField(Employee, related_name='services')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
