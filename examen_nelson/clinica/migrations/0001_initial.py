# Generated by Django 3.2.8 on 2021-12-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre', max_length=120)),
                ('cantidad', models.IntegerField(help_text='cant stock', max_length=120)),
                ('precio', models.FloatField(help_text='precio', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre', max_length=50)),
                ('dueño', models.CharField(help_text='Nombre', max_length=50)),
                ('tipo', models.CharField(help_text='Tipo de mascota', max_length=50)),
                ('raza', models.CharField(help_text='Raza', max_length=50)),
                ('edad', models.IntegerField(help_text='Edad', verbose_name=int)),
            ],
        ),
    ]
