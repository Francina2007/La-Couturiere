# Generated by Django 3.2.25 on 2025-06-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MODA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lacouturière',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_marcas/'),
        ),
    ]
