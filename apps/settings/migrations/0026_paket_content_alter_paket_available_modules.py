# Generated by Django 5.0.1 on 2024-02-21 12:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0025_paket_available_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='paket',
            name='content',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание тарифа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paket',
            name='available_modules',
            field=models.IntegerField(default=2, verbose_name='Доступное количество модулей'),
        ),
    ]