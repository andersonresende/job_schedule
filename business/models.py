from django.db import models


class CategoryEmployee(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)


class Employee(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    category_employee = models.ForeignKey(CategoryEmployee)


class CategoryService(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)


class Service(models.Model):
    name = models.CharField(max_length=750, null=True, blank=True)
    category_service = models.ForeignKey(CategoryService)
