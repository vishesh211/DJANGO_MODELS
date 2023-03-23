import re
from django.shortcuts import render
from . import models
# Create your views here.

all_patients = models.Patient.objects.all()

context = {
    'patients':all_patients
}

def list_patient(request):
    return render(request,'office/list.html',context=context)