from django.shortcuts import render, get_object_or_404,redirect
from webapp.models import Entry
from webapp.forms import EntryForm, SearchForm

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


def entry_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = EntryForm(data={
            'name': entry.name,
            'email': entry.email,
            'text': entry.text}
                        )
        return render(request, 'edit.html', context={
            'form': form,
            'entry': entry
        })
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.name=form.cleaned_data['name']
            entry.email=form.cleaned_data['email']
            entry.text=form.cleaned_data['text']
            entry.save()
            return redirect('index')
        else:
            return render(request, 'edit.html', context={
                'form': form,
                'entry': entry
            })


def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {
            'entry': entry
        })
    elif request.method == 'POST':
        entry.delete()
        return redirect('index')


def entry_search(request):
    query = request.GET.get('form')
    entry = Entry.objects.filter(name__contains=query)
    return render(request, 'search.html', {'entry': entry})


