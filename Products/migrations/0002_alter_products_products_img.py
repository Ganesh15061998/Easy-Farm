# Generated by Django 4.2 on 2023-04-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='products_Img',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
    ]
