# Generated by Django 5.0.6 on 2024-06-04 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_livros_ano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='ano',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='numPaginas',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='sinopse',
        ),
    ]