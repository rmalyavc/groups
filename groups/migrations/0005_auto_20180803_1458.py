# Generated by Django 2.1 on 2018-08-03 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20180803_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to='groups.Group', verbose_name='Родительская группа'),
        ),
    ]
