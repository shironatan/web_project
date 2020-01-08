# Generated by Django 2.2.6 on 2019-11-27 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_auto_20191121_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(verbose_name='rating')),
                ('contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Contents', verbose_name='作品名')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー名')),
            ],
            options={
                'db_table': 'Recommend',
            },
        ),
    ]
