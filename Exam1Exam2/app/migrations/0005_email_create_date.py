# Generated by Django 3.2.1 on 2021-05-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210506_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]