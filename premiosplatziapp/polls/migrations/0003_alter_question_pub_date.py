# Generated by Django 4.0.1 on 2022-02-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
