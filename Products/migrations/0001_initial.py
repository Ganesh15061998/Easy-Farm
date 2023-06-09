# Generated by Django 4.2 on 2023-04-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_Img', models.ImageField(upload_to='uploads/')),
                ('products_Name', models.CharField(max_length=50)),
                ('products_Availability', models.CharField(max_length=50)),
                ('products_Price', models.CharField(max_length=20)),
                ('products_Description', models.TextField()),
            ],
        ),
    ]
