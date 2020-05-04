# Generated by Django 2.1.5 on 2020-05-04 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('F', 'Found Item'), ('L', 'Lost Item')], default='Found Item', max_length=1)),
                ('location', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=16)),
                ('image', models.FileField(upload_to='')),
                ('identification_mark', models.TextField(help_text='Separate each item by comma')),
                ('secret_information', models.TextField(help_text='Separate each item by comma')),
                ('tags', models.CharField(choices=[('0', 'keys'), ('1', 'cards'), ('2', 'books')], default='keys', max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-update'],
            },
        ),
    ]
