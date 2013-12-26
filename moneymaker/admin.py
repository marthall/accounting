from django.contrib import admin

from moneymaker.models import Product
from moneymaker.models import Income
from moneymaker.models import Expense
from moneymaker.models import ExpenseCategory
from moneymaker.models import IncomeCategory


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', '__unicode__')


admin.site.register(Product)
admin.site.register(Income)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
