# Generated by Django 5.0.4 on 2024-04-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_alter_recetas_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='categoria',
            field=models.CharField(choices=[('Recetas', 'Recetas'), ('Saladas', 'Saladas'), ('Dulces', 'Dulces')], default='Recetas', max_length=100),
        ),
    ]
