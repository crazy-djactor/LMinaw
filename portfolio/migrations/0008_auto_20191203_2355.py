# Generated by Django 2.2.5 on 2019-12-03 22:55

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20191203_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='cover',
            field=sorl.thumbnail.fields.ImageField(upload_to='', verbose_name='couverture'),
        ),
    ]
