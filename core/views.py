from django.shortcuts import render
from .models import *
from .forms import *
def home(request):
    table = Odam.objects.all()
    context ={
        'table':table
    }
    return render(request,"index.html",context)
def form(request):
    context={}
    if request.method == 'GET':
        context['form'] = OdamForm
        return render(request,"form.html", context=context)

    else:
        forms = OdamForm(request.POST)
        if forms.is_valid():
            forms.save()
            context['form'] = OdamForm()
            return render(request,'form.html',context=context)