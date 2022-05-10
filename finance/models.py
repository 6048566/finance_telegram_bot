from django.db import models

# Create your models here.

class Currency(models.Model):
    class Meta:
        db_table = 'currencies'
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    title = models.CharField(max_length=20, blank=False, null=False, verbose_name='Title')
    short_title = models.CharField(max_length=4, blank=False, null=False, verbose_name='Short title')


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=30, blank=False, null=False, verbose_name='Title')
    is_spend = models.BooleanField(default=False, verbose_name='Spend')


class FinanceLog(models.Model):
    class Meta:
        db_table = 'finance_logs'
        verbose_name = 'Finance log'
        verbose_name_plural = 'finance logs'

    chat_id = models.CharField(max_length=20, blank=False, null=False, verbose_name='Chat ID')
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category')
    currency = models.ForeignKey(Currency, blank=False, null=False, verbose_name='Currency')
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name='Amount')
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Description')