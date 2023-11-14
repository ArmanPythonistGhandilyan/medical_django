from django.db import models

class BookedAppointment(models.Model):
    name = models.CharField("Full name", max_length=50)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone", max_length=13) # the max length of armenian number e.g. +374-77-77-77
    date = models.DateField("Booked date")
    message = models.TextField("Message", blank=True)

    def __str__(self) -> str:
        return self.name