# Generated by Django 5.0.4 on 2024-04-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_alter_recetas_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='index'),
        ),
    ]
