from django import forms
from .models import BookedAppointment

class BookedAppointmentForm(forms.ModelForm):
    class Meta:
        model = BookedAppointment
        fields = ["name", "email", "phone", "date", "message"]