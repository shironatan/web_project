# Generated by Django 2.2.6 on 2019-11-20 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191120_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='details',
        ),
        migrations.AddField(
            model_name='contents',
            name='contents_detail',
            field=models.CharField(max_length=100, null=True, verbose_name='詳細'),
        ),
    ]