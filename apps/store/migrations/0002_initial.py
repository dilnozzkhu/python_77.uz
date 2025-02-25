# Generated by Django 5.1.1 on 2025-01-21 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads', to='users.seller', verbose_name='seller'),
        ),
        migrations.AddField(
            model_name='photo',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='store.ad', verbose_name='ad'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='store.category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads', to='store.subcategory', verbose_name='sub category'),
        ),
    ]
