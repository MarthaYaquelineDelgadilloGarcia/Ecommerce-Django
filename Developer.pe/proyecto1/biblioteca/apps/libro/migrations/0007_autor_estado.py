# Generated by Django 2.1.5 on 2021-07-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0006_libro_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]