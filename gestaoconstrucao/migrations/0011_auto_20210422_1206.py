# Generated by Django 3.1.7 on 2021-04-22 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoconstrucao', '0010_auto_20210422_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='Produtos1',
        ),
        migrations.AddField(
            model_name='venda',
            name='Produtos1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='gestaoconstrucao.eletricos', verbose_name='Produtos Eletricos'),
        ),
    ]