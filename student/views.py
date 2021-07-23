from django.shortcuts import render
from .forms import StudentRegistrationForm

# Create your views here.
def register_student(request):
        forms=StudentRegistrationForm()
        return render(request,"register_student.html",{"forms":forms})
