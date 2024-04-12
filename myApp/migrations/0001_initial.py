# Generated by Django 5.0.4 on 2024-04-12 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoUsuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_isbn', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=10)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='libros/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='myApp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('nombreApellido', models.CharField(max_length=200)),
                ('tipoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='myApp.categoriausuario')),
            ],
        ),
    ]