from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Studentrecord
from multiprocessing import context


# Create your views here.

def Home(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        form.save()

        return redirect('showdata')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def Delete_record(request, Student_id):
    a = Studentrecord.objects.get(pk=Student_id)
    a.delete()
    return redirect('showdata')


def Update_record(request, Student_id):
    if request.method == 'POST':
        data = Studentrecord.objects.get(pk=Student_id)
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('showdata')

    else:
        data = Studentrecord.objects.get(pk=Student_id)
        form = StudentForm(instance=data)

    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


def Showdata(request):
    data = Studentrecord.objects.all()

    context = {
        # 'form': form,
        'data': data,
    }
    return render(request, 'showdata.html', context)
