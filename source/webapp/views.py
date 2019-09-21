from django.shortcuts import render, get_object_or_404,redirect
from webapp.models import Entry
from webapp.forms import EntryForm

# Create your views here.


def entry_view(request, *args, **kwargs):
    entry = Entry.objects.all().order_by('-time_create').filter(status='active')
    return render(request, 'index.html', context={
        'entry': entry
    })


def entry_create(request, *args, **kwargs):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = Entry.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={
                'form': form
            })

