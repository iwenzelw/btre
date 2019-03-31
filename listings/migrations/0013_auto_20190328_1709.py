# Generated by Django 2.1.7 on 2019-03-28 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_auto_20190327_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50, unique=True, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.AlterModelOptions(
            name='listing',
            options={},
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Bedrooms', verbose_name='Квартиры'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='district',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.District', verbose_name='МикроРайон'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor', verbose_name='Риелтор'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.State', verbose_name='Район'),
        ),
    ]
