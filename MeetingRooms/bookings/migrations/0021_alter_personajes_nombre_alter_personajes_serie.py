# Generated by Django 5.0.4 on 2024-05-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0020_remove_personajes_fecha_personajes_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajes',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='personajes',
            name='serie',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
