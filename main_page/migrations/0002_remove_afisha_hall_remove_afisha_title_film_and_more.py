# Generated by Django 4.2.7 on 2023-11-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afisha',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='afisha',
            name='title_film',
        ),
        migrations.AddField(
            model_name='afisha',
            name='place',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='afisha',
            name='title_product',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
