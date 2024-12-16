from django.contrib import admin
from .models import ClarificationType, ClarificationCategory, ClarificationFiles, General, Assign_To, Rfx

# Register your models here.
admin.site.register(ClarificationType)
admin.site.register(ClarificationCategory)
admin.site.register(General)
admin.site.register(Assign_To)
admin.site.register(Rfx)
admin.site.register(ClarificationFiles)
