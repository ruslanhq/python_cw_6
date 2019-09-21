# Generated by Django 2.2 on 2019-09-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(max_length=2000, verbose_name='Post text')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')),
                ('time_edit', models.DateTimeField(auto_now=True, verbose_name='Editing time')),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=20, verbose_name='Status')),
            ],
        ),
    ]