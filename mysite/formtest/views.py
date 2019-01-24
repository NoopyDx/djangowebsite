from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MailForm, MailForm2

def index(request):
    formValid, form2Valid = False, False
    msg = { 'v' : 'Virus', 'a' : 'AntiVirus'}

    if request.method=='POST' and 'btn' in request.POST:
        form = MailForm(request.POST)
        form.save()
        if form.is_valid():
            formValid = form.is_valid()

    if request.method=='POST' and 'btn2' in request.POST:
        form2 = MailForm2(request.POST)
        form2.save()
        if form2.is_valid():
            form2Valid = form2.is_valid()


    form = MailForm()
    form2 = MailForm2()

    context = {
        'form' : form,
        'form2': form2,
        'formValid' : formValid,
        'form2Valid' : form2Valid,
        'msg' : msg,
    }
    return render(request, 'formtest/index.html',context)
