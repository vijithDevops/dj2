# Generated by Django 2.1.2 on 2018-11-08 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20181102_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcardupproducts',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vcloud_brand_data', to='App.rcardBrands'),
        ),
        migrations.AlterField(
            model_name='rcardupproducts',
            name='fileid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vcloud_file_data', to='App.rcarduplogs'),
        ),
    ]
