# Generated by Django 2.2.5 on 2019-10-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191001_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturisticos',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracoes'),
        ),
    ]