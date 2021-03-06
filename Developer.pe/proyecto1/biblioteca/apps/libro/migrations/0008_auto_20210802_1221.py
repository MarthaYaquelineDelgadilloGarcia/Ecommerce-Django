# Generated by Django 2.1.5 on 2021-08-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_autor_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]
