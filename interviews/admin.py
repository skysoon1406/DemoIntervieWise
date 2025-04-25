from django.contrib import admin
from .models import Interview
# Register your models here.

class InterviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Interview,InterviewAdmin)




# 也可以寫作：因為 register   有自帶默認 功能，沒填寫就會自帶 ModelAdmin 的 class
# admin.site.register(Interview)