# Generated by Django 5.0.4 on 2024-04-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_alter_recetas_categoria_alter_recetas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='dulces',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='saladas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
