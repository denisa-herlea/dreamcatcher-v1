from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .charts import StressChartCreator, EnergyChartCreator, DurationChartCreator
from .forms import UserForm
from .models import Dream
from django.contrib import messages
from django.db.models.functions import TruncDate
from django.db.models import Avg


def login_page(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return descriere_categorie(request)
    return render(request, 'login.html')


def login_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            user = authenticate(username=username, password=password)
            if user is None:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname)
                user.save()
                return render(request, 'success_register.html')
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})


def login_register_view(request):
    return render(request, 'register.html')


def descriere_categorie(request):
    return render(request, 'descriere_categorie.html')


def rating(request):
    if request.method == 'POST':
        description = request.POST['description']
        category = request.POST['category']
        user = request.user.username
        dream = Dream(user=user, descriere=description, eticheta=category, stres=0, nivelEnergie=0, durata=0)
        dream.save()
    return render(request, 'rating.html')


@login_required
def statistici_view(request):
    if request.method == 'POST':
        duration = request.POST['duration']
        energy = request.POST['energy']
        stress = request.POST['stress']
        user = request.user.username

        dream = Dream.objects.latest('id')
        dream.durata = duration
        dream.nivelEnergie = energy
        dream.stres = stress
        dream.save()
    return render(request, 'statistici.html')


def back_to_statistici_view(request):
    return render(request, 'statistici.html')


def statistici_view_stres(request):
    chart_creator = StressChartCreator()
    return chart_creator.create_chart(request)


def statistici_view_energie(request):
    chart_creator = EnergyChartCreator()
    return chart_creator.create_chart(request)


def statistici_view_durata(request):
    chart_creator = DurationChartCreator()
    return chart_creator.create_chart(request)
