from django.shortcuts import render
from .forms import StudRegistration
from .models import Stud

# Create your views here.
def new_disp(request):
    if request.method == 'POST':
        fm = StudRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['stud_name']
            db = fm.cleaned_data['stud_dob']
            cl = fm.cleaned_data['stud_class']
            reg = Stud(stud_name = nm, stud_dob = db, stud_class=cl)
            reg.save()
            fm = StudRegistration()
    else:
        fm = StudRegistration()
        stud = Stud.objects.all()
    return render(request, "newanddisp.html", {'form': fm, 'stu': stud})

