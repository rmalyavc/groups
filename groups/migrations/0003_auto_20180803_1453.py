# Generated by Django 2.1 on 2018-08-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20180803_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elem',
            options={'ordering': ['name'], 'verbose_name': 'Элемент', 'verbose_name_plural': 'Элементы'},
        ),
        migrations.AlterField(
            model_name='elem',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/icons/%Y/%m/%d/', verbose_name='Элемент'),
        ),
    ]