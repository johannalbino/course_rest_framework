# Generated by Django 2.2.5 on 2019-09-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturisticos',
            old_name='status',
            new_name='aprovado',
        ),
        migrations.AddField(
            model_name='pontoturisticos',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.atracoes'),
        ),
    ]
