# Generated by Django 4.2.7 on 2023-12-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_idare'),
    ]

    operations = [
        migrations.AddField(
            model_name='idare',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='idare'),
        ),
    ]
