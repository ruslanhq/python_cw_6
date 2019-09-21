from django.db import models

# Create your models here.
ENTRY_STATUS = (
    ('active', 'Active'),
    ('blocked', 'Blocked')
)


class Entry(models.Model):
    name = models.CharField(max_length=40, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(max_length=2000, verbose_name='Post text')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')
    time_edit = models.DateTimeField(auto_now=True, verbose_name='Editing time')
    status = models.CharField(max_length=20, verbose_name='Status', choices=ENTRY_STATUS, default=ENTRY_STATUS[0][0])

    def __str__(self):
        return self.name



