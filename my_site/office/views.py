import re
from django.shortcuts import render
from . import models
# Create your views here.

office_list = models.Patient.objects.all()

def list_patient(request):
    return render(request,'office/list.html')