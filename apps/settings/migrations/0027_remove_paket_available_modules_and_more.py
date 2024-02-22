# Generated by Django 5.0.1 on 2024-02-22 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0026_paket_content_alter_paket_available_modules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paket',
            name='available_modules',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='selected_paket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.paket'),
        ),
    ]
