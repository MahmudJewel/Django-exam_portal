from django.contrib import admin
from admn.models import Course, Question #, Result

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
#admin.site.register(Result)