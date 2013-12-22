from django.contrib import admin

from moneymaker.models import Product
from moneymaker.models import Income
from moneymaker.models import Outcome
from moneymaker.models import Category


class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('date', '__unicode__')


admin.site.register(Product)
admin.site.register(Income)
admin.site.register(Outcome, OutcomeAdmin)
admin.site.register(Category)
