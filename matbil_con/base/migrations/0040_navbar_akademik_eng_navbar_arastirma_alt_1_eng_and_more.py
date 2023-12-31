# Generated by Django 4.2.7 on 2023-12-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_navbar_bolum_alt_4_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='akademik_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='arastirma_alt_1_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='arastirma_alt_2_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='arastirma_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='ders_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='home_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='kalite_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='mezun_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='program_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='navbar',
            name='staj_eng',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
