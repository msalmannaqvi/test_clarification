from django.shortcuts import render
from .forms import ClarificationForm, ClarificationFileform, RfxForm, AssignForm, GeneralForm, ClarificationTypeForm
from .models import General, ClarificationFiles
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def home(request):
    clari = ClarificationFiles.objects.all()
    obj = General.objects.all()
    return render(request, 'home.html', {'obj':obj, 'clari':clari})
def category(request):
    form = ClarificationTypeForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'category.html', {'form':form})
def category(request):
    form = ClarificationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'home.html', {'form': form})


def rfx(request):
    form = RfxForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'home.html', {'form': form})
def assign_to(request):
    form = AssignForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'home.html', {'form': form})
def general(request):
    form = GeneralForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'home.html', {'form': form})
# def type_view(request):
#     form = C(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     return render(request, 'home.html', {'form': form})
