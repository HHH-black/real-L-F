# Generated by Django 3.0.4 on 2020-05-06 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0002_tag_slug'),
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
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-update'],
            },
        ),
    ]
