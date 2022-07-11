from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Show
from .form import ShowForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')

def shows(request):
    # print('SHOWS: ', Show.objects.all())
    # return HttpResponse(
    #     '<h1>TV Shows</h1>'
    # )
    shows = Show.objects.all()
    return render(request, 'shows_list.html', {'shows': shows})

def show_create(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show = form.save()
            return redirect('shows')
    else:
        form = ShowForm()
    context = {'form': form, 'header': 'Add new tv show'}
    return render(request, 'show_form.html', context)

def show_edit(request, pk):
    show = Show.objects.get(pk = pk) # primary key
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            show = form.save()
            return redirect('shows')
    else:
        form = ShowForm(instance=show)
    return render(request, 'show_form.html', {'form': form})

def show_delete(request, pk):
    Show.objects.get(pk=pk).delete()
    return redirect('shows')