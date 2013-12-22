from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Outcome(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.product.name


class Income(models.Model):
    @staticmethod
    def get_total_income(self):
        return sum(self.income_set.all())
