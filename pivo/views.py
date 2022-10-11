from django.shortcuts import render
from django.http import HttpResponse
from .models import vitrina
from .forms import *

def index(request):
    # Блок вывода витрины...
    marka = vitrina.objects.filter(pk=2)
    birka = vitrina.objects.filter(pk=2)
    cena = vitrina.objects.filter(pk=2)
    col = vitrina.objects.filter(pk=2)

    # Блок вывода и валидации формы ввода...
    sum = 0
    while True:
        if request.method == "POST":
            form = mony(request.POST)
            if form.is_valid():
                nom = form.cleaned_data.get('nomin_mony')

                if nom == 1:
                    sum += nom
                    return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col, 'form': form, 'sum': sum})


                if nom == 2:
                    sum += nom
                    return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col, 'form': form, 'sum': sum})

                if nom == 5:
                    sum += nom
                    return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col, 'form': form, 'sum': sum})
                if nom == 10:
                    sum += nom
                    return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col, 'form': form, 'sum': sum})
                else:
                    error = "Вы ввели неверный номинал монеты..."
                    form = mony()
                    return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col, 'form': form,'error': error})
        else:
            form = mony()
            return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col, 'form': form})




    return render(request, 'pivo/list.html',{'marka': marka, 'birka': birka, 'cena': cena, 'col': col})























