# Generated by Django 2.1.7 on 2019-03-26 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20190326_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.State'),
        ),
    ]
