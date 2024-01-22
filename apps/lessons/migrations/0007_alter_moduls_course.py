# Generated by Django 5.0.1 on 2024-01-20 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_remove_courses_course_name_en_and_more'),
        ('lessons', '0006_alter_moduls_options_alter_lesson_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduls',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.courses', verbose_name='Курс'),
        ),
    ]
