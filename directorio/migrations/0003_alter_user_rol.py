# Generated by Django 4.1.1 on 2022-10-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0002_remove_user_adress_remove_user_phone_user_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(choices=[('administrador', 'administrador'), ('secretario', 'secretario'), ('planificador', 'planificador')], max_length=25, verbose_name='rol'),
        ),
    ]
