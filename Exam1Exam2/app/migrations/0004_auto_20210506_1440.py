# Generated by Django 3.2.1 on 2021-05-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_date_todo_list_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list',
            name='datetime',
        ),
        migrations.AddField(
            model_name='todo_list',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo_list',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
