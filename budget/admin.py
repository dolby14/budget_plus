from django.contrib import admin

# Register your models here.
from budget.models import Budget, Capital_equip,Salaryy,Investigation1,Investigation2,Consumable

admin.site.register(Budget)

admin.site.register(Capital_equip)

admin.site.register(Salaryy)

admin.site.register(Investigation1)

admin.site.register(Investigation2)

admin.site.register(Consumable)


