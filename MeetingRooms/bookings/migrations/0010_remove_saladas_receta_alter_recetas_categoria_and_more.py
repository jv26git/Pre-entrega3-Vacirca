# Generated by Django 5.0.4 on 2024-04-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_dulces_imagen_saladas_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saladas',
            name='receta',
        ),
        migrations.AlterField(
            model_name='recetas',
            name='categoria',
            field=models.IntegerField(choices=[('0', 'Recetas'), ('1', 'Saladas'), ('2', 'Dulces')], default='0'),
        ),
        migrations.DeleteModel(
            name='Dulces',
        ),
        migrations.DeleteModel(
            name='Saladas',
        ),
    ]
