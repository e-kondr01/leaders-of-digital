from django.contrib import admin
from django.apps import apps

from .models import *

# Register your models here.
admin.site.register(Organization)
admin.site.register(Subdivision)
admin.site.register(Object)
admin.site.register(Support)
admin.site.register(Order)
admin.site.register(DefectType)
admin.site.register(SupportDefect)
admin.site.register(SafetyGroup)
admin.site.register(Worker)
