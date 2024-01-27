# Generated by Django 4.2.8 on 2024-01-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0021_alter_userprofile_clas"),
    ]

    operations = [
        migrations.AddField(
            model_name="paket",
            name="price",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Цена тарифа"
            ),
        ),
        migrations.AddField(
            model_name="paket",
            name="slug",
            field=models.SlugField(
                default=1, max_length=255, unique=True, verbose_name="Авто URL"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="paket",
            name="title_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Название тарифа"
            ),
        ),
        migrations.AddField(
            model_name="paket",
            name="title_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Название тарифа"
            ),
        ),
        migrations.AddField(
            model_name="settings",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Описание сайта"),
        ),
        migrations.AddField(
            model_name="settings",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Описание сайта"),
        ),
        migrations.AddField(
            model_name="settings",
            name="title_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Название сайта"
            ),
        ),
        migrations.AddField(
            model_name="settings",
            name="title_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Название сайта"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="suptitle2_en",
            field=models.CharField(
                blank=True,
                help_text="Возможность подготовиться в любое время",
                max_length=255,
                null=True,
                verbose_name="Подзаголовок слайдера 2",
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="suptitle2_ru",
            field=models.CharField(
                blank=True,
                help_text="Возможность подготовиться в любое время",
                max_length=255,
                null=True,
                verbose_name="Подзаголовок слайдера 2",
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="suptitle3_en",
            field=models.CharField(
                blank=True,
                help_text="99% наших выпусников являются стипендиатами",
                max_length=255,
                null=True,
                verbose_name="Подзаголовок слайдера 3",
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="suptitle3_ru",
            field=models.CharField(
                blank=True,
                help_text="99% наших выпусников являются стипендиатами",
                max_length=255,
                null=True,
                verbose_name="Подзаголовок слайдера 3",
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="suptitle_en",
            field=models.CharField(
                blank=True,
                help_text="Уроки на кыргызском языке",
                max_length=255,
                null=True,
                verbose_name="Подзаголовок слайдера 1",
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="suptitle_ru",
            field=models.CharField(
                blank=True,
                help_text="Уроки на кыргызском языке",
                max_length=255,
                null=True,
                verbose_name="Подзаголовок слайдера 1",
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="title_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Загаловок слайдера"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="title_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Загаловок слайдера"
            ),
        ),
        migrations.AddField(
            model_name="teachers",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Описание преподавателя"),
        ),
        migrations.AddField(
            model_name="teachers",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Описание преподавателя"),
        ),
        migrations.AddField(
            model_name="teachers",
            name="name_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Имя Преподавателя"
            ),
        ),
        migrations.AddField(
            model_name="teachers",
            name="name_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Имя Преподавателя"
            ),
        ),
    ]