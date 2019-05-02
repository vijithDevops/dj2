# Generated by Django 2.1.2 on 2018-10-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20181012_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='adverisements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usertype', models.CharField(default='User', max_length=50)),
                ('ctype', models.CharField(default='Vcloud', max_length=50)),
                ('adtype', models.CharField(default='Image', max_length=50)),
                ('adimage', models.ImageField(blank=True, null=True, upload_to='ads/%y%m%d')),
                ('adtext', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'adverisements',
            },
        ),
    ]
