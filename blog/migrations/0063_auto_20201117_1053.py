# Generated by Django 3.0.5 on 2020-11-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0062_auto_20201117_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
