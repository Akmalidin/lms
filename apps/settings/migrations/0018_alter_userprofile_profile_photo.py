# Generated by Django 4.2.8 on 2023-12-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0017_alter_userprofile_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_photo",
            field=models.ImageField(blank=True, null=True, upload_to="profile_photos/"),
        ),
    ]