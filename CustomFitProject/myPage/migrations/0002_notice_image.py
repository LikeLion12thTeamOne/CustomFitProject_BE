# Generated by Django 5.0.7 on 2024-07-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notices/'),
        ),
    ]
