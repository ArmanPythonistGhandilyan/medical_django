from django.contrib import admin
from .models import BookedAppointment

class BookedAppointmentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]
admin.site.register(BookedAppointment, BookedAppointmentAdmin)    
