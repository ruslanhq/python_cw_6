from django.shortcuts import render
from webapp.models import Entry

# Create your views here.


def entry_view(request, *args, **kwargs):
    entry = Entry.objects.all().order_by('-time_create').filter(status='active')
    return render(request, 'index.html', context={
        'entry': entry
    })
