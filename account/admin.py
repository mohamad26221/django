from django.contrib import admin
from.models import CustomUser

admin.site.register(CustomUser)


admin.site.site_header = 'التسجيل في السكن'
admin.site.site_title = 'university'
admin.site.site_url = "التسحيل في السكن"
