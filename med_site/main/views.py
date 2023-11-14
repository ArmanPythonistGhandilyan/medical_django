from django.shortcuts import render, redirect
from .forms import BookedAppointmentForm
from .models import BookedAppointment
from django.http import Http404

def main(request):
    if request.method == "POST":
        form = BookedAppointmentForm(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect(request.path_info)
        else:
            print(form.errors)     
    # else:
    #     form = BookedAppointmentForm()
    return render(request, "main/main.html")