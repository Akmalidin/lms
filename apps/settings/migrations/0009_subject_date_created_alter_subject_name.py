# Generated by Django 4.2.8 on 2023-12-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0008_subject_alter_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название предмета"),
        ),
    ]
