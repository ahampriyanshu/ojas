# Generated by Django 3.0.5 on 2020-11-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_delete_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.TextField(default=None)),
            ],
        ),
    ]