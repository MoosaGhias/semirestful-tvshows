from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show, ShowManager
# Create your views here.
#this shows what the initial page looks like
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')
def create(request):
    if request.method == 'POST':
        errors = Show.objects.show_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new')
        Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']

        )
    return redirect('/')

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)

def show(request, show_id):
    one_show = Show.objects.get(id= show_id)
    context = {'show':one_show}
    return render(request, 'show.html', context)
    
def delete(request, show_id):
    one_show = Show.objects.get(id= show_id)
    one_show.delete()
    return redirect('/')

def update(request, show_id):
    if request.method == 'POST':
        errors = Show.objects.show_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/{show_id}/edit')
        one_show = Show.objects.get(id= show_id)
        one_show.title = request.POST['title']
        one_show.network = request.POST['network']
        one_show.release_date = request.POST['release_date']
        one_show.description = request.POST['description']
        one_show.save()
    return redirect('/')