# Generated by Django 3.1.7 on 2021-04-22 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoconstrucao', '0008_remove_venda_exemplo_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='nome',
        ),
    ]